import cv2


def blur_region(frame, x, y, w, h, margin=0.4):
    """Pixelate-blur a box expanded by `margin` to cover the whole head, in place."""
    H, W = frame.shape[:2]
    dx, dy = int(w * margin), int(h * margin)
    x0, y0 = max(0, x - dx), max(0, y - dy)
    x1, y1 = min(W, x + w + dx), min(H, y + h + dy)
    roi = frame[y0:y1, x0:x1]
    if roi.size == 0:
        return
    small = cv2.resize(roi, (max(1, (x1 - x0) // 16), max(1, (y1 - y0) // 16)))
    frame[y0:y1, x0:x1] = cv2.resize(small, (x1 - x0, y1 - y0), interpolation=cv2.INTER_NEAREST)
