from NNetwork import NNetwork
from StochasticHillClimbing import StochasticHillClimbing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

network=NNetwork()

#########################
# z trenowaniem sieci
#########################
network.train()
network.plotBoundary(network.predict)
x=network.generateMeshgrid()
y=network.predict(x)[:,1]
y=np.reshape(y,(len(y),1))
y_df=pd.DataFrame(y)
y_df.to_csv('y.txt')

#########################
# bez trenowania sieci
#########################
# x=network.generateMeshgrid()
# y_df=pd.read_csv('y.txt')
# y=np.array(y_df)[:,1]
# y=y.reshape((len(y),1))

#########################
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