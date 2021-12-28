import sys, json, numpy as np
import cv2, urllib, time
import autoBot
from urllib import request

bot = autoBot.Control()


i = 1
while True:

    if i % 2 == 0:
        si = str(i)
        urllib.request.urlretrieve("http://localhost:8000/", "pic/nodeImg" + si + ".png")
        time.sleep(0.1)
        try:
            print("image number {}".format(i))
            frame = cv2.imread("pic/nodeImg" + si + ".png", 0)

            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            img_counter = 0

            # resizing for faster detection

            frame = cv2.resize(frame, (640, 480))
            # using a greyscale picture, also for faster detection
            x1 = None
            x_1 = None
            y_1 = None
            y1 = None

            cv2.imshow("f", frame)



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

                bot.send_commands(distance, x_1, y_1)
                cv2.imshow("f", frame)

            else:
                bot.send_commands(0,0,0)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            img_counter += 1

        except Exception as e:
            print(str(e))
    i += 1

cv2.destroyAllWindows()

