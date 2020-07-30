import time

import cv2
from cv2 import aruco


def display_detected(frame, rate):
    # ディスプレイ用フォント
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "f: {}".format(round(rate, 1)), (0,64), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow("tracking aruco", frame)


#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("/dev/v4l/by-id/usb-KYE_Systems_Corp._USB_Camera_200901010001-video-index0")
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)
f = "1280x720_params.yaml"
fs = cv2.FileStorage(f, cv2.FILE_STORAGE_READ)
mat = fs.getNode("camera_matrix").mat()
dist = fs.getNode("distortion_coefficients").mat()
mlen = 250

last_time = time.monotonic()
n = 0
sum_fps = 0
sum_process_time = 0
sum_inference_time = 0

while True:
    start_time = time.monotonic()

    _, frame = cap.read()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, dictionary)
    retval, rvec, tvec = aruco.estimatePoseSingleMarkers(corners, mlen, mat, dist)

    end_time = time.monotonic()
    n += 1
    sum_fps += 1.0 / (end_time - last_time)
    sum_process_time += 1000 * (end_time - start_time)

    last_time = end_time
    text_line = 'Aruco: IO: %.2fms TrueFPS: %.2f ' % (
        sum_process_time / n, sum_fps / n
    )
<<<<<<< HEAD
    # print(text_line)
    display_detected(frame, sum_fps/n)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
=======
    print(text_line)
>>>>>>> 503f9492acc0bc86d4c6c59fc9179b90686230a1
