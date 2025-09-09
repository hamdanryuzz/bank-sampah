from pathlib import Path
import shutil
from sklearn.model_selection import train_test_split

BASE_DIR = Path("TACO_YOLO")
OUT_BASE = Path("datasets")
OUT_BASE.mkdir(parents=True, exist_ok=True)

images = list(BASE_DIR.glob("*.jpg"))
labels = list(BASE_DIR.glob("*.txt"))

train, test = train_test_split(images, test_size=0.2, random_state=42)
train, val = train_test_split(train, test_size=0.1, random_state=42)

def move(files, split):
    img_dir = OUT_BASE / split / "images"
    lbl_dir = OUT_BASE / split / "labels"
    img_dir.mkdir(parents=True, exist_ok=True)
    lbl_dir.mkdir(parents=True, exist_ok=True)

    for img in files:
        lbl = BASE_DIR / (img.stem + ".txt")
        shutil.copy(img, img_dir / img.name)
        shutil.copy(lbl, lbl_dir / lbl.name)

move(train, "train")
move(val, "valid")
move(test, "test")

print(" Dataset sudah dipisah ke 'datasets/'")
