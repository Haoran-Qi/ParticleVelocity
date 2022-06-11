import numpy as np
import math

class Particel:
    def __init__(self, points):
        self.position = [0,0]
        self.area = len(points)

# 1. 先图像灰度的求平均值， 找到异常的值，把灰度图转化为0和1的异常图
# 2. 找出聚集在一起的异常点，可以同过面积进行筛选噪声点
# 3. particle的中心可以用 (x_difference/2, y_difference / 2) 来估计
class ImageParser:
    def __init__(self, img):
        self.map = self.preprocessImg(img)
        self.visitedMap = np.zeros(self.map.shape)
        self.direction =[[1,0],[-1,0],[0,-1],[0,1]]
    
    def preprocessImg(self, img):
        meanValue = np.mean(img)
        abnormalMatrix = np.zeros(img.shape)
        abnormalMatrix.fill(meanValue)
        abnormalMatrix = np.absolute(np.subtract(img,abnormalMatrix))
        # we regard abnormal particel as 3 * std
        threshold = 3 * math.ceil(np.std(abnormalMatrix))
        abnormalMatrix = (abnormalMatrix > threshold).astype(int)
        return abnormalMatrix

    def bfs(self, y, x):
        group = []
        queue = [[y,x]]
        self.visitedMap[y][x] = 1

        while queue:
            cur = queue.pop(0)
            group.append(cur)
            for cor in self.direction:
                newY += cor[0]
                newX += cor[1]

                if newY < 0 or newY >= self.map.shape[0] or newX < 0 or newX >= self.map.shape[1]:
                    continue
                if self.visitedMap[newY][newX]:
                    continue
                
                self.visitedMap[newY][newX] = 1
                queue.append([newY,newX])        
        return group

    def gatheringPoints(self):
        candidates = []
        for y in map:
            for x in map:
                self.bfs(y,x)

        return candidates
