import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

# Creates the window object
webcam = cv2.VideoCapture(0)
webcam.set(3, 1280)
webcam.set(4, 720)

# Creates the HandDetector object
detector = HandDetector(detectionCon=0.8, maxHands=2)

# playing the frame through a while loop
while True:
    success, img = webcam.read()
    # To flip the image on the axis 1 (vertical) to avoid mirror effect
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    # If there is a hand on the screen:
    if hands:
        landmark_list = hands[0]["lmList"]

        # Index Finger
        tip_index = landmark_list[8][0:2]
        cv2.circle(img, tip_index, radius=10, color=(200, 0, 0), thickness=cv2.FILLED)
        cvzone.putTextRect(img, "Index", tip_index, scale=2, thickness=1, offset=0,
                           colorR=(200, 0, 0), colorT=(255, 255, 255))

        # Middle Finger
        tip_middle = landmark_list[12][0:2]
        cv2.circle(img, tip_middle, radius=10, color=(0, 0, 0), thickness=cv2.FILLED)
        cvzone.putTextRect(img, "Middle", tip_middle, scale=2, thickness=1, offset=0,
                           colorR=(0, 0, 0), colorT=(255, 255, 255))

        # Ring Finger
        tip_ring_finger = landmark_list[16][0:2]
        cv2.circle(img, tip_ring_finger, radius=10, color=(0, 0, 200), thickness=cv2.FILLED)
        cvzone.putTextRect(img, "Ring", tip_ring_finger, scale=2, thickness=1, offset=0,
                           colorR=(0, 0, 200), colorT=(255, 255, 255))

        # Little Finger
        tip_little_finger = landmark_list[20][0:2]
        cv2.circle(img, tip_little_finger, radius=10, color=(0, 200, 200), thickness=cv2.FILLED)
        cvzone.putTextRect(img, "Little", tip_little_finger, scale=2, thickness=1, offset=0,
                           colorR=(0, 200, 200), colorT=(255, 255, 255))

        tip_thumb = landmark_list[4][0:2]
        cv2.circle(img, tip_thumb, radius=10, color=(255, 255, 255), thickness=cv2.FILLED)
        cvzone.putTextRect(img, "Thumb", tip_thumb, scale=2, thickness=1, offset=0,
                           colorR=(255, 255, 255), colorT=(0, 0, 0))

    cv2.imshow("Webcam Image", img)
    # setting the refreshment delay for the frame
    cv2.waitKey(1)
