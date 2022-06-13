import numpy as np
import math
import cv2
import pdb
import argparse
from Particel import ImageParser
from plot import drawTrajectory


def locateParticals(img, particleCount, particleColor):
    ip = ImageParser(img, particleCount, particleColor)
    particles = ip.generateParticles()

    ### draw detected particles ###
    # reversedCenter = [(int(p.getCenter()[1]), int(p.getCenter()[0])) for p in particles]
    # radius = 15
    # color = (0,0, 255)
    # thickness = 2
    # for center in reversedCenter:
    #     image = cv2.circle(img, center, radius, color, thickness)
    # cv2.imshow("detected", image)

    return particles


def analyzeMovements(imgPre, imgCur):
    return []


def processVideo(
    path, frameGap, particleCount, particleColor="dark", startFrame=None, endFrame=None
):
    cap = cv2.VideoCapture(path)
    fps = math.ceil(cap.get(cv2.CAP_PROP_FPS))
    totalFrame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    if not startFrame:
        startFrame = 0
    if not endFrame:
        endFrame = totalFrame

    print("====================================")
    print("Start processing video " + path)
    print("FPS: " + str(fps))
    print("Total Frams: " + str(totalFrame))
    print("Gap Frames: " + str(frameGap))

    # processing video
    frameCount = startFrame
    coordinates = []
    while frameCount < endFrame:
        ret, frame = cap.read()

        if (
            frameCount < startFrame
            or frameCount > endFrame
            or frameCount % frameGap != 0
        ):
            print(
                "---------------"
                + "Skipped Frame #"
                + str(frameCount)
                + "---------------"
            )
            frameCount += 1
            continue

        print(
            "---------------"
            + "Processing Frame #"
            + str(frameCount)
            + "---------------"
        )

        centers = locateParticals(frame, particleCount, particleColor)
        coordinates.append({"centers": centers, "frame": frameCount})

        frameCount += 1

    cap.release()
    cv2.destroyAllWindows()

    print("Video Processed")
    print("====================================")

    return coordinates


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(dest="path", type=str, help="absolute path to the video file")
    parser.add_argument(
        dest="frameGap",
        type=int,
        help="how many frame to skip to detect",
    )
    parser.add_argument(
        dest="particleCount",
        type=int,
        help="the number of particles in the video",
    )
    parser.add_argument(
        "-particleColor", type=str, help="dark or light", default="dark"
    )
    parser.add_argument("-start", type=int, default=None)
    parser.add_argument("-end", type=int, default=None)
    args = parser.parse_args()
    coordinates = processVideo(
        args.path,
        args.frameGap,
        args.particleCount,
        args.particleColor,
        args.start,
        args.end,
    )
    pdb.set_trace()
    drawTrajectory([1080, 1920], coordinates)

# python VideoParser.py 1.mp4 2 7 -start 510 -end 630
