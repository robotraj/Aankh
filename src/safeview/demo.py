"""Stage 0 demo: blur every detected face. Only the blurred frame is shown or recorded."""
import os
import time

import cv2

from .blur import blur_region


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise SystemExit("Cannot open webcam")
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    writer = None
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        for (x, y, w, h) in detector.detectMultiScale(gray, 1.1, 4):
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
