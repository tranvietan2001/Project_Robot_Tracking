import cv2

# cap = cv2.VideoCapture(0)
video = "./Project_Robot_Tracking/video_test.mp4"
cap = cv2.VideoCapture(video)

while True:
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow("Window Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
