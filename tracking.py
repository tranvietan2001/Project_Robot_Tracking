import cv2

# cap = cv2.VideoCapture(0)
video = "/home/antv/Desktop/CodeCV/Project_Robot_Tracking/img/test.mp4"
cap = cv2.VideoCapture(video)
# tracker = cv2.legacy.TrackerMOSSE.create()
tracker = cv2.legacy.TrackerCSRT.create()
ret, frame = cap.read()
# lay toa do keo tha chuot
# bbox = cv2.selectROI("track", frame, False)
# print(bbox)
# ----------------
# toa do tuy chinh\
# vide_test.mp4
# x = 810
# y = 359
# w = 33
# h = 22
# bbox = (x,y,w,h)
# cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) 
# ----------------
# test.mp4
x = 190
y = 136
w = 138
h = 144
bbox = (x,y,w,h)
cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) 

print("Seleck bbox: ",bbox)
tracker.init(frame, bbox)
while True:
    ret,frame = cap.read()
    if not ret:
        break
    success, bbox = tracker.update(frame)
    if success:
        # print(bbox)
        x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
        print(x,y)
    else:
        print("object lost")
    cv2.imshow("Window Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
