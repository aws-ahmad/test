"""Streamlit interface for USB camera YOLOv8 object detection."""

from __future__ import annotations

import threading
from pathlib import Path

import av
import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit_webrtc import VideoProcessorBase, WebRtcMode, webrtc_streamer
from ultralytics import YOLO


@st.cache_resource
def load_model(model_path: str) -> YOLO:
    return YOLO(model_path)


class YoloVideoProcessor(VideoProcessorBase):
    def __init__(self, model: YOLO, conf: float, imgsz: int) -> None:
        self.model = model
        self.conf = conf
        self.imgsz = imgsz
        self._lock = threading.Lock()

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        image = frame.to_ndarray(format="bgr24")

        with self._lock:
            results = self.model.predict(
                source=image,
                conf=self.conf,
                imgsz=self.imgsz,
                verbose=False,
            )

        annotated = results[0].plot()
        return av.VideoFrame.from_ndarray(annotated, format="bgr24")


def main() -> None:
    if get_script_run_ctx() is None:
        print(
            "This app must be started with 'streamlit run streamlit_app.py' "
            "so Streamlit can create a session context."
        )
        return

    st.set_page_config(page_title="YOLOv8 USB Camera", layout="wide")
    st.title("YOLOv8 USB Camera Object Detection")
    st.write("Start the camera stream to run live detection in your browser.")

    with st.sidebar:
        st.header("Settings")
        model_path = st.text_input("Model path", value="yolov8n.pt")
        conf = st.slider("Confidence threshold", min_value=0.05, max_value=0.95, value=0.30)
        imgsz = st.selectbox("Inference image size", options=[320, 480, 640, 960], index=2)

    model = load_model(str(Path(model_path)))

    webrtc_streamer(
        key="yolov8-webcam",
        mode=WebRtcMode.SENDRECV,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=lambda: YoloVideoProcessor(model=model, conf=conf, imgsz=imgsz),
        async_processing=True,
    )


if __name__ == "__main__":
    main()
