import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
fourcc = fourcc.to_bytes(4, 'little').decode('utf-8')
print("FOURCC=" + str(fourcc))

fps    = int(cap.get(cv2.CAP_PROP_FPS))
print("FPS=" + str(fps))

cap.release()
