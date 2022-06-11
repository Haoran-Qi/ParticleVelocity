import numpy as np
import math
import cv2
import pdb

from Particel import ImageParser

# set np print with no limitations
# np.set_printoptions(threshold=np.inf)


def locateParticals(img):
    ImageParser(img)

    pdb.set_trace()


def analyzeMovements(imgPre, imgCur):
    return []


def processVideo(path, frameGap):
    cap = cv2.VideoCapture(path)
    fps = math.ceil(cap.get(cv2.CAP_PROP_FPS))
    totalFrame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print("====================================")
    print("Start processing video " + path)
    print("FPS: " + str(fps))
    print("Total Frams: " + str(totalFrame))
    print("Gap Frames: " + str(frameGap))

    # processing video
    frameCount = 0
    while cap.isOpened():

        if frameCount % frameGap == 0:
            ret, frame = cap.read()
            # covert to gray scale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            locateParticals(gray)
            # pdb.set_trace()
            # cv2.imshow("frame", gray)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        frameCount += 1

    cap.release()
    cv2.destroyAllWindows()


processVideo("1.mp4", 6)
# locateParticals(np.array([[5,5,5],[5,5,5],[5,5,1000]]))
