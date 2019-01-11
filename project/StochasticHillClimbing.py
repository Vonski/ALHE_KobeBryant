import numpy as np
from random import normal

class StochasticHillClimbing:

    def __init__(self, x, y, real_points):
        self.z=0.0
        self.min_accuracy=0.7
        self.max_x = 300
        self.max_y = 800
        self.min_x = -300
        self.min_y = -50
        self.data=np.concatenate((x,y), axis=1)
        self.real_points=real_points

    def getCutPoints(self):
        cut_points=np.full((self.max_x-self.min_x, self.max_y-self.min_y), -1.0)
        for p in self.data:
            if p[2]>=self.z:
                cut_points[(int(p[0])-self.min_x),(int(p[1])-self.min_y)]=p[2]
        return cut_points

    def climb(self):
        z_tmp=0.0
        best_rate=0.0
        cnt=0
        while True:
            self.z_temp=abs(normal(scale=0.1))+self.z
            points=###
            rate_tmp=self.rateSolution(points)
            if rate_temp>best_rate:
                best_rate=rate_tmp
                self.z=z.tmp
                cnt=0
            else:
                cnt+=1
            if cnt>100:
                break
        return points        


    def rateSolution(self, points):
        if self.getRealPointsMean(points)<self.min_accuracy:
            return 0
        else:
            return self.getArea(points)
    
    def getArea(self, points):
        return len(points)

    def getRealPointsMean(self,points):
        points_to_avg=np.array()
        for p in points:
            for r in self.real_points:
                if p[0]]==r[0] and p[1]==r[1]:
                points_to_avg.append[r]
        return points_to_avg[:,2].mean()

