# import pyardrone
import time
# import test
import sys, json, numpy as np


class Control:


    def send_commands(self, distance, width, height):
        try:
            d = distance
            a = width
            h = height

            print("distance: {}, width: {}, height: {}".format(d,a,h))
            # drone.navdata_ready.wait()
            # while not drone.state.fly_mask:
            #     drone.takeoff()
            #     # print("1")
            #     # break

            if (d * 3) > 200:
                file = open("commands.js", "w")
                file.write("client.front(0.2);\n")
                file.close()
                # drone.move(forward=0.2)  # move forward at full speed
                # drone.move(cw=0)
                print("distance={} result=move forward".format(d))
            elif 20 > d > 0:
                file = open("commands.js", "w")
                file.write("client.back(0.2);\n")
                file.close()
                # drone.move(backward=0.1)
                # drone.move(cw=0)
                print("distance={} result=backward".format(d))
            else:
                file = open("commands.js", "w")
                file.write("client.front(0);client.back(0);\n")
                file.close()
                # drone.move(backward=0.1)
                # drone.move(cw=0)
                print("distance={} result=backward".format(d))

            # print(distance)

            if a < 90:

                file = open("commands.js", "a")
                file.write("client.counterClockwise(0.2);\n")
                file.close()

                print("angle={} rotate left".format(a))
                # drone.move(ccw=0.2)
            elif a > 300:
                file = open("commands.js", "a")
                file.write("client.clockwise(0.2);\n")
                file.close()

                print("angle={} rotate right".format(a))
                # drone.move(cw=0.2)
            else:
                file = open("commands.js", "a")
                file.write("client.counterClockwise(0);client.clockwise(0);\n")
                file.close()

                # drone.move(cw=0)
                # drone.move(ccw=0)
                print("stop rotating")

            if h < 50:
                file = open("commands.js", "a")
                file.write("client.down(0.1);")
                file.close()

                print("tilt down")
                # drone.move(down=0.1)

            elif h > 270:
                file = open("commands.js", "a")
                file.write("client.up(0.1);")
                file.close()
                # drone.move(up=0.1)
                print("tilt up")
            else:
                file = open("commands.js", "a")
                file.write("client.up(0);client.down(0);")
                file.close()

                print("no z-axis movement")
                # drone.move(down=0)
                # drone.move(up=0)
            time.sleep(0.01)
        except Exception as e:
            print(str(e))
