import numpy as np
import math
import cv2
import pdb

# set np print with no limitations
np.set_printoptions(threshold=np.inf)

# 1. 先图像灰度的求平均值， 找到异常小的值，把灰度图转化为0和1的异常图
# 2. 找出聚集在一起的异常点，可以同过面积进行筛选噪声点
# 3. particle的中心可以用 (x_difference/2, y_difference / 2) 来估计
def locateParticals(img):
    return []


def analyzeMovements(imgPre,imgCur):
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
            pdb.set_trace()
            cv2.imshow("frame", gray)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        frameCount += 1

    cap.release()
    cv2.destroyAllWindows()


processVideo("1.mp4", 6)
