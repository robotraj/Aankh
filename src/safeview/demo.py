"""Stage 0 demo: blur every detected face. Only the blurred frame is shown or recorded."""
import os
import time

import cv2

from .blur import blur_region

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "face_detection_yunet_2023mar.onnx")


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise SystemExit("Cannot open webcam")
    detector = cv2.FaceDetectorYN.create(MODEL_PATH, "", (320, 320), score_threshold=0.5)
    writer = None
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        detector.setInputSize((frame.shape[1], frame.shape[0]))
        _, faces = detector.detect(frame)
        for f in (faces if faces is not None else []):
            x, y, w, h = (int(v) for v in f[:4])
            blur_region(frame, x, y, w, h)
        # `frame` is already blurred here; nothing unblurred is displayed or saved.
        if writer is not None:
            writer.write(frame)
        cv2.imshow("SafeView (strict baseline)", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        if key == ord("r"):
            if writer is None:
                os.makedirs("recordings", exist_ok=True)
                h_, w_ = frame.shape[:2]
                writer = cv2.VideoWriter(f"recordings/{int(time.time())}.mp4",
                                         cv2.VideoWriter_fourcc(*"mp4v"), 20, (w_, h_))
            else:
                writer.release()
                writer = None
    if writer is not None:
        writer.release()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
