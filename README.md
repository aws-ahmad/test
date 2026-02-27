# USB Camera + YOLOv8 Object Detection

This project opens a USB camera, runs YOLOv8 object detection, and draws boxes/labels on each frame in real time.

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

## 3) Run detection

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
3. Run `camera_yolov8.py` from the IDE.
4. Make sure your USB camera is connected and not already in use.

Press **q** in the preview window to stop the app.
