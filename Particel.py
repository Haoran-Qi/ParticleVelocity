import numpy as np
import math
from matplotlib import pyplot as plt
import pdb


class Particel:
    def __init__(self, points):
        self.points = points

        maxY = max(self.points, key=lambda p: p[0])[0]
        minY = min(self.points, key=lambda p: p[0])[0]
        maxX = max(self.points, key=lambda p: p[1])[1]
        minX = min(self.points, key=lambda p: p[1])[1]

        self.center = [(maxY+minY)/2, (maxX+minX)/2]
    def getCenter(self):
        return self.center

class ImageParser:
    def __init__(self, img, particleCount, particleColor="dark"):
        self.particleColor = particleColor
        self.particleCount = particleCount
        self.map = self.preprocessImg(img)
        self.visitedMap = np.zeros(self.map.shape)
        self.direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    def preprocessImg(self, img):
        abnormalMatrix = np.copy(img)
        mean = np.mean(abnormalMatrix)
        # we regard abnormal particel as 3 * std
        cutOff = 2.5 * np.std(abnormalMatrix)
        if self.particleColor == "dark":
            abnormalMatrix = np.where((abnormalMatrix > mean - cutOff), 0, 1)
        else:
            abnormalMatrix = np.where((abnormalMatrix < mean + cutOff), 0, 1)

        ### show abnormal Matrix ###
        # plt.imshow(abnormalMatrix)
        # plt.show()
        # pdb.set_trace()
        return abnormalMatrix

    def bfs(self, y, x):
        group = []
        queue = [[y, x]]
        self.visitedMap[y][x] = 1
        while queue:
            cur = queue.pop(0)
            group.append(cur)
            for cor in self.direction:
                newY = cur[0] + cor[0]
                newX = cur[1] + cor[1]
                if (
                    newY < 0
                    or newY >= self.map.shape[0]
                    or newX < 0
                    or newX >= self.map.shape[1]
                ):
                    continue
                if self.visitedMap[newY][newX]:
                    continue
                if self.map[newY][newX] > 0:
                    self.visitedMap[newY][newX] = 1
                    queue.append([newY, newX])
        return group

    def gatheringPoints(self):
        candidates = []
        for y in range(self.map.shape[0]):
            for x in range(self.map.shape[1]):
                if self.map[y][x] > 0 and self.visitedMap[y][x] == 0:
                    candidate = self.bfs(y, x)
                    if len(candidate) > 3:
                        candidates.append(candidate)
        sortedCandidates = sorted(candidates, key=lambda x: len(x), reverse=True)[
            : self.particleCount
        ]
        return sortedCandidates

    def generateParticles(self):
        pointsGroup = self.gatheringPoints()
        particles = [Particel(points) for points in pointsGroup]
        return particles
