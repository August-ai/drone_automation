import socket
import sys
import time
import cv2
# import pyardrone
import numpy as np


class Control:

    # drone = pyardrone.ARDrone()

    def takeoff(self):
        self.drone.navdata_ready.wait()
        while not self.drone.state.fly_mask:
            # self.drone.takeoff()
            print("1")
            break

    def land(self):
        while self.drone.state.fly_mask:
            self.drone.land()




control = Control


def autonomous(self, frame, hog, img_counter):
    x1 = None
    x_1 = None
    y_1 = None
    y1 = None
    if img_counter % 32 == 0:

        boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4))

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        for (xA, yA, xB, yB) in boxes:
            x_1 = xA
            x1 = xB
            y_1 = yA
            y1 = yB
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
            break
        boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4))

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        for (xA, yA, xB, yB) in boxes:
            x_1 = xA
            x1 = xB
            y_1 = yA
            y1 = yB
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
            break

        if x1 is not None:
            KNOWN_DISTANCE = 60.96

            KNOWN_WIDTH = 150

            p = (543.45 * x1) / 60
            focalLength = (p * KNOWN_DISTANCE) / KNOWN_WIDTH
            distance = (KNOWN_WIDTH * 543.45) / p

            file = open("commands.js", "w")
            file.write("{}\n{}\n{}".format(distance, x_1, y_1))

            cv2.imshow("Image", frame)

            img_name = "photos/frame{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            print(img_counter)

            file.close()



# #import urllib
# import time, cv2
# for i in range(100):
#   ...:     si = str(i)
#   ...:     urllib.request.urlretrieve("http://localhost:8000/", "pic/nodeImg" + si + ".png")
#   ...:     time.sleep(0.2)
#
# import numpy as np
# for i in range(100):
#   ...:     si = str(i)
#   ...:     cap = cv2.VideoCapture("pic/nodeImg" + si + ".png")
#   ...:     #
#   ...:     hog = cv2.HOGDescriptor()
#   ...:     hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#   ...:     #
#   ...:     #
#   ...:     img_counter = 1
#   ...:     # p = 0
#   ...:     while True:
#   ...:         #
#   ...:         #
#   ...:         try:
#   ...:             ret, frame = cap.read()
#   ...:
#   ...:             frame = cv2.resize(frame, (640, 480))
#   ...:             gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#   ...:             x1 = None
#   ...:             x_1 = None
#   ...:             y_1 = None
#   ...:             y1 = None
#   ...:             cv2.imshow("f", frame)
#   ...:             #
#   ...:             if img_counter % 1 == 0:
#   ...:
#   ...:                 boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4))
#   ...:
#   ...:                 boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
#   ...:                 for (xA, yA, xB, yB) in boxes:
#   ...:                     x_1 = xA
#   ...:                     x1 = xB
#   ...:                     y_1 = yA
#   ...:                     y1 = yB
#   ...:                     # display the detected boxes in the colour picture
#   ...:                     cv2.rectangle(frame, (xA, yA), (xB, yB),
#   ...:                                   (0, 255, 0), 2)
#   ...:                     break
#   ...:                 boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4))
#   ...:
#   ...:                 boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
#   ...:                 for (xA, yA, xB, yB) in boxes:
#   ...:                     x_1 = xA
#   ...:                     x1 = xB
#   ...:                     y_1 = yA
#   ...:                     y1 = yB
#   ...:                     # display the detected boxes in the colour picture
#   ...:                     cv2.rectangle(frame, (xA, yA), (xB, yB),
#   ...:                                   (0, 255, 0), 2)
#   ...:                     break
#   ...:
#   ...:                 if x1 is not None:
#   ...:                     KNOWN_DISTANCE = 60.96
#   ...:
#   ...:                     KNOWN_WIDTH = 150
#   ...:
#   ...:                     p = (543.45 * x1) / 60
#   ...:                     focalLength = (p * KNOWN_DISTANCE) / KNOWN_WIDTH
#   ...:                     distance = (KNOWN_WIDTH * 543.45) / p
#   ...:
#   ...:                     file = open("commands.js", "w")
#   ...:                     file.write("{}\n{}\n{}".format(distance, x_1, y_1))
#   ...:
#   ...:                     cv2.imshow("Image", frame)
#   ...:
#   ...:                     img_name = "photos/frame{}.png".format(img_counter)
#   ...:                     cv2.imwrite(img_name, frame)
#   ...:                     print("{} written!".format(img_name))
#   ...:                     print(img_counter)
#   ...:
#   ...:                     file.close()
#   ...:             #
#   ...:             if cv2.waitKey(1) & 0xFF == ord('q'):
#   ...:                 break
#   ...:             img_counter += 1
#   ...:         except Exception as e:
#   ...:             print(str(e))
#   ...:
#   ...:     # When everything done, release the capture
#   ...:     cap.release()
#   ...:     cv2.destroyAllWindows()