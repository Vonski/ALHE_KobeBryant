import numpy as np
import collections

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
	
	def updateQ(self, q, current, c):
		if (current[0]-1,current[1]) in c:
			q.append((current[0]-1,current[1]))
			c.remove((current[0]-1,current[1]))
		if (current[0]+1,current[1]) in c:
			q.append((current[0]+1,current[1]))
			c.remove((current[0]+1,current[1]))
		if (current[0],current[1]-1) in c:
			q.append((current[0],current[1]-1))
			c.remove((current[0],current[1]-1))
		if (current[0],current[1]+1) in c:
			q.append((current[0],current[1]+1))
			c.remove((current[0],current[1]+1))
		return q, c

	def getBiggestArea(self, z):
		found = True
		marea = []
		carea = []
		q = collections.deque()
		c = set([tuple(x) for x in np.argwhere(z>-1)])
		if c:
			current = c.pop()
		else:
			found = False
		while(found):
			q, c = self.updateQ(q,current,c)
			carea.append([current[0], current[1], z[current[0], current[1]]])
			if q:
				current = q[0]
				q.popleft()
			elif c:
				if len(marea)<len(carea):
					marea=carea
				carea = []
				current = c.pop()
			else:
				if len(marea)<len(carea):
					marea=carea
				found = False
		return marea
