from NNetwork import NNetwork
from StochasticHillClimbing import StochasticHillClimbing
import numpy as np

network=NNetwork()
network.train()
network.plotBoundary(network.predict)
x=network.generateMeshgrid()
y=network.predict(x)
real_points=np.concatenate((network.X, network.Y), axis=1)
climber=StochasticHillClimbing(x,y,real_points)
z=climber.getCutPoints()
print(z)
print(z[300,50])
climber.z=0.5
print(climber.getCutPoints())
climber.z=1.0
print(climber.getCutPoints())
