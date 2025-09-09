
# Deteksi Jenis Sampah






1. Bikin virtual environment
```bash
  python -m venv venv
  venv\Scripts\activate
```
2. install requirements
```bash
  pip install -r requirements.txt
```

3. Download Dataset (3GB+)

```bash
  git clone https://github.com/pedropro/TACO.git
  cd TACO
  python3 download.py / py download.py
```

4. Training YOLO

```bash
  pip install ultralytics
  yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
```
