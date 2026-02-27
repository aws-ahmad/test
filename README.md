# USB Camera + YOLOv8 Object Detection

This project provides two ways to run YOLOv8 object detection with a USB camera:

1. **Streamlit web interface** (recommended)
2. **Desktop OpenCV window script**

## 1) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 2) Install dependencies

```bash
pip install -r requirements.txt
```

## 3) Run Streamlit interface (web UI)

```bash
streamlit run streamlit_app.py
```

Then open the local URL shown by Streamlit (usually `http://localhost:8501`), allow camera permissions, and start the stream.

Streamlit settings (left sidebar):

- `Model path` (default `yolov8n.pt`)
- `Confidence threshold`
- `Inference image size`

## 4) (Optional) Run desktop script

```bash
python camera_yolov8.py
```

Optional arguments:

- `--camera-index 0` (choose another index if needed)
- `--model yolov8n.pt` (use custom YOLOv8 weights)
- `--conf 0.3` (confidence threshold)
- `--imgsz 640` (inference image size)

Example:

```bash
python camera_yolov8.py --camera-index 1 --model yolov8s.pt --conf 0.4
```

## Notes for PyCharm

1. Open this folder in PyCharm.
2. Configure the project interpreter to use your `.venv`.
3. For Streamlit, create a **Run Configuration** of type **Python** with:
   - Script path: `<venv>/Scripts/streamlit.exe` (Windows) or `<venv>/bin/streamlit` (Linux/macOS)
   - Parameters: `run streamlit_app.py`
   - Working directory: project root
4. Alternatively, run Streamlit in the PyCharm terminal:
   - `streamlit run streamlit_app.py`
5. `camera_yolov8.py` can still be run as a normal Python run configuration.
6. Make sure your USB camera is connected and not already in use.
