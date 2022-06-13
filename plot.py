from matplotlib import pyplot as plt
import cv2
import numpy as np
import pdb

def drawTrajectory(shape, coordinates):
    img = np.zeros([shape[0],shape[1],3],dtype=np.uint8)
    img.fill(255)

    # drawing arrows
    previousCtr = coordinates[0]["centers"]
    for i in range(1, len(coordinates)):
        centers =  coordinates[i]["centers"]
        # pdb.set_trace()
        for j in range(len(centers)):
            img = cv2.arrowedLine(img, (int(previousCtr[j][1]),int(previousCtr[j][0])), (int(centers[j][1]), int(centers[j][0])) , (0,0, 255), 5)
        previousCtr = centers
    
    cv2.imshow('1 Channel Window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 


# drawTrajectory([1080, 1920], [{"centers":[[0,0],[1079, 0]]}, {"centers":[[1079,1919],[0, 1919]]}])