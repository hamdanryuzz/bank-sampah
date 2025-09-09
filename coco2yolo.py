import json, os, shutil
from pathlib import Path
from PIL import Image
from sklearn.model_selection import train_test_split

# Path dataset TACO
ANNOT_FILE = "TACO/data/annotations.json"
IMG_DIR = Path("TACO/data")
OUT_DIR = Path("TACO_YOLO")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Kategori organik
organic_classes = [
    "food waste", "vegetable", "fruit", "leaf", "banana peel",
    "egg shell", "nut shells"
]

def map_class(name: str):
    return 0 if name.lower() in organic_classes else 1

# Load JSON
with open(ANNOT_FILE, "r") as f:
    data = json.load(f)

images = {img["id"]: img for img in data["images"]}
categories = {cat["id"]: cat["name"] for cat in data["categories"]}

for ann in data["annotations"]:
    img_id = ann["image_id"]
    img_info = images[img_id]
    img_file = IMG_DIR / img_info["file_name"]

    if not img_file.exists():
        continue

    im = Image.open(img_file)
    w, h = im.size

    cat_name = categories[ann["category_id"]]
    cls_id = map_class(cat_name)

    x, y, bw, bh = ann["bbox"]
    xc, yc = (x + bw / 2) / w, (y + bh / 2) / h
    nw, nh = bw / w, bh / h

    label_path = OUT_DIR / (img_file.stem + ".txt")
    with open(label_path, "a") as f:
        f.write(f"{cls_id} {xc:.6f} {yc:.6f} {nw:.6f} {nh:.6f}\n")

    shutil.copy(img_file, OUT_DIR / img_file.name)

print("✅ Konversi selesai! Semua label & gambar ada di", OUT_DIR)
