from NNetwork import NNetwork
from StochasticHillClimbing import StochasticHillClimbing

network=NNetwork()
network.train()
network.plotBoundary(network.predict)
x=network.generateMeshgrid()
y=network.predict(x)
climber=StochasticHillClimbing(x,y)
z=climber.getCutPoints()
print(z)
print(z[300,50])
climber.z=0.5
print(climber.getCutPoints())
climber.z=1.0
print(climber.getCutPoints())
