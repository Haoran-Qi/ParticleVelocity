import numpy as np
import math
import cv2
import pdb

# set np print with no limitations
np.set_printoptions(threshold=np.inf)


def processVideo(path, timeGap):
    cap = cv2.VideoCapture(path)
    fps = math.ceil(cap.get(cv2.CAP_PROP_FPS))
    totalFrame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    gapFrames = fps / timeGap

    # processing video
    frameCount = 0
    while cap.isOpened():

        if frameCount % gapFrames == 0:
            ret, frame = cap.read()
            # covert to gray scale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            pdb.set_trace()
            cv2.imshow("frame", gray)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        frameCount += 1

    cap.release()
    cv2.destroyAllWindows()


processVideo("1.mp4")
