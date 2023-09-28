# import cv2
# import cvlib as cvl
# from cvlib.object_detection import draw_bbox
# # from gtts import gTTS
# # from playsound import playsound

# video = cv2.VideoCapture(1)

# while True:
#     ret, frame = video.read()
#     bbox, label, conf = cvl.detect_common_objects(frame)
#     out_img = draw_bbox(frame, bbox, label, conf)
#     cv2.imshow("Object Detection", out_img)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# video.release()
# cv2.destroyAllWindows()

import cv2
image = cv2.VideoCapture(0)
# image = cv2.imread('/home/antv/Desktop/CodeCV/Project_Robot_Tracking/img/img4.jpg')

# initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# detect humans in input image
(humans, _) = hog.detectMultiScale(image, winStride=(10, 10),
padding=(32, 32), scale=1.1)

# getting no. of human detected
print('Human Detected : ', len(humans))

# loop over all detected humans
for (x, y, w, h) in humans:
   pad_w, pad_h = int(0.15 * w), int(0.01 * h)
   cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

# display the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()