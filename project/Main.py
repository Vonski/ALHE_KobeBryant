from NNetwork import NNetwork
from StochasticHillClimbing import StochasticHillClimbing
import Modifier as mod
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import model_from_json


network=NNetwork()

cx1 = 141
cy1 = 200
md1 = mod.generateAvarageValuesTable(network.x_data, network.y_data,cx1,cy1)

# cx2 = 65
# cy2 = 100
# md2 = mod.generateAvarageValuesTable(network.x_data, network.y_data,cx2,cy2)

# cx3 = 24
# cy3 = 36
# md3 = mod.generateAvarageValuesTable(network.x_data, network.y_data,cx3,cy3)

# cx4 = 12
# cy4 = 18
# md4 = mod.generateAvarageValuesTable(network.x_data, network.y_data,cx4,cy4)

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
# model z pliku
#########################
# load json and create model
# json_file = open('model52.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights('model52.h5')
# network.model=loaded_model
# network.plotBoundary(network.predict)
# x=network.generateMeshgrid()
# y=network.predict(x)[:,1]
# y=np.reshape(y,(len(y),1))

for iy in range(900):
	for ix in range(600):
		y[iy*600+ix,0] *= md1[math.floor(ix/(600/cx1)),math.floor(iy/(900/cy1))]
		# y[iy*600+ix,0] *= md2[math.floor(ix/(600/cx2)),math.floor(iy/(900/cy2))]
		# y[iy*600+ix,0] *= md3[math.floor(ix/(600/cx3)),math.floor(iy/(900/cy3))]
		# y[iy*600+ix,0] *= md4[math.floor(ix/(600/cx4)),math.floor(iy/(900/cy4))]
			
# cs = plt.contourf( np.arange(-300, 300, 1),np.arange(-100, 800, 1), y.reshape((900,600)), 50, cmap=plt.cm.Spectral)
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