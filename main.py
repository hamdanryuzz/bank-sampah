import cv2
from ultralytics import YOLO


def get_available_camera(max_index=5):
    for i in range(max_index):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  
        if cap.isOpened():
            cap.release()
            return i
    return None

camera_index = get_available_camera()
if camera_index is None:
    print("❌ Tidak ada kamera yang tersedia!")
    exit()
print(f"✅ Menggunakan kamera index: {camera_index}")


model_path = "runs/detect/train2/weights/best.pt"
model = YOLO(model_path)


cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("❌ Gagal membuka kamera")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠ Gagal membaca frame, keluar...")
        break

    results = model.predict(frame, conf=0.3)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Realtime", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
