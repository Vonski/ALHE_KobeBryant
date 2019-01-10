import numpy as np

class StochasticHillClimbing:

    def __init__(self, x, y):
        self.z=0.0
        self.min_accuracy=0.7
        self.max_x = 300
        self.max_y = 800
        self.min_x = -300
        self.min_y = -50
        self.data=np.concatenate((x,y), axis=1)

    def getCutPoints(self):
        cut_points=np.full((self.max_x-self.min_x, self.max_y-self.min_y), -1.0)
        for p in self.data:
            if p[2]>=self.z:
                cut_points[(int(p[0])-self.min_x),(int(p[1])-self.min_y)]=p[2]
        return cut_points

    def climb(self):
        pass

    def rateSolution(self, points):
        if points[:,2].mean()<self.min_accuracy:
            return 0
        else:
            return self.getArea(points)
    
    def getArea(self, points):
        return len(points)
