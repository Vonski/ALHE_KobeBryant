from NNetwork import NNetwork
from StochasticHillClimbing import StochasticHillClimbing

network=NNetwork()
climber=StochasticHillClimbing()
network.train()
network.plotBoundary(network.predict)
x=network.generateMeshgrid()
y=network.predict(x)
z=climber.getCutPoints(y)
print(z)
climber.z=0.5
print(climber.getCutPoints(y))
climber.z=1.0
print(climber.getCutPoints(y))
