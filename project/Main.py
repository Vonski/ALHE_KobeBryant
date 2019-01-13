from NNetwork import NNetwork
from StochasticHillClimbing import StochasticHillClimbing
import numpy as np
import matplotlib.pyplot as plt

network=NNetwork()
network.train()
#network.plotBoundary(network.predict)
x=network.generateMeshgrid()
y=network.predict(x)[:,1]
y=np.reshape(y,(len(y),1))
print(max(y))
real_points=np.concatenate((network.x_data, network.y_data), axis=1)
climber=StochasticHillClimbing(x,y,real_points)
points=climber.climb()
print(points)
print(points.shape)
#z=np.reshape(points[:,2],(len(points),1))
#plt.scatter(points[:,0], points[:,1])
print(len(np.arange(-300,300)))
plt.contourf( np.arange(-50, 800, 1), np.arange(-300, 300, 1),points, 2, cmap=plt.cm.Spectral)
plt.show()