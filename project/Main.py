from NNetwork import NNetwork
from StochasticHillClimbing import StochasticHillClimbing
import Modifier as mod
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

network=NNetwork()

cx = 281
cy = 400

md = mod.generateAvarageValuesTable(network.x_data, network.y_data,cx,cy)
print(md[33:38,7:13])

#########################
# z trenowaniem sieci
#########################
# network.train()
# network.plotBoundary(network.predict)
# x=network.generateMeshgrid()
# y=network.predict(x)[:,1]
# y=np.reshape(y,(len(y),1))
# y_df=pd.DataFrame(y)
# y_df.to_csv('y.txt')

#########################
# bez trenowania sieci
#########################
x=network.generateMeshgrid()
y_df=pd.read_csv('y.txt')
y=np.array(y_df)[:,1]
y=y.reshape((len(y),1))

# for iy in range(900):
	# for ix in range(600):
		# y[iy*600+ix,0] *= md[math.floor(ix/(600/cx)),math.floor(iy/(900/cy))]

# print(np.arange(-300, 300, 1).shape)
# print(np.arange(-100, 800, 1).shape)
# print(y.reshape((600,900)).shape)
			
# cs = plt.contourf( np.arange(-300, 300, 1),np.arange(-100, 800, 1), y.reshape((900,600)), 10, cmap=plt.cm.Spectral)
# plt.colorbar(cs)
# plt.show()

#########################
real_points=np.concatenate((network.x_data, network.y_data), axis=1)
climber=StochasticHillClimbing(x,y,real_points)
points=climber.climb()
print(points)
print(points.shape)
#z=np.reshape(points[:,2],(len(points),1))
#plt.scatter(points[:,0], points[:,1])
print(len(np.arange(-300,300)))
plt.contourf( np.arange(-300, 300, 1), np.arange(-100, 800, 1), points.T, 0, cmap=plt.cm.Spectral)
plt.show()