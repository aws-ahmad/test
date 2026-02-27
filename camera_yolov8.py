"""Open a USB camera, run YOLOv8 object detection, and draw boxes in real time."""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run YOLOv8 detection on a USB camera stream.",
    )
    parser.add_argument(
        "--camera-index",
        type=int,
        default=0,
        help="USB camera index (default: 0)",
    )
    parser.add_argument(
        "--model",
        type=Path,
        default=Path("yolov8n.pt"),
        help="Path to YOLOv8 model weights (default: yolov8n.pt)",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.3,
        help="Confidence threshold (default: 0.3)",
    )
    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Inference image size (default: 640)",
    )
    return parser.parse_args()


def run() -> None:
    args = parse_args()

    model = YOLO(str(args.model))

    cap = cv2.VideoCapture(args.camera_index)
    if not cap.isOpened():
        raise RuntimeError(
            f"Could not open USB camera at index {args.camera_index}."
        )

    window_name = "YOLOv8 USB Camera Detection"
    print("Press 'q' to quit.")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Warning: failed to read frame from camera.")
                break

            results = model.predict(
                source=frame,
                conf=args.conf,
                imgsz=args.imgsz,
                verbose=False,
            )

            annotated = results[0].plot()
            cv2.imshow(window_name, annotated)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
