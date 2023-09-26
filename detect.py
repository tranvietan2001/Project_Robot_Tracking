import cv2
import cvlib as cvl
from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# from playsound import playsound

video = cv2.VideoCapture(1)

while True:
    ret, frame = video.read()
    bbox, label, conf = cvl.detect_common_objects(frame)
    out_img = draw_bbox(frame, bbox, label, conf)
    cv2.imshow("Object Detection", out_img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()