import numpy as np

class StochasticHillClimbing:

    def __init__(self):
        self.z=0.0

    def getCutPoints(self, points):
        return np.extract(points>self.z,points)