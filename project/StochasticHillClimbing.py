import numpy as np
from random import normalvariate
import collections
import matplotlib.pyplot as plt

class StochasticHillClimbing:

	def __init__(self, x, y, real_points):
		self.z=1.0
		self.z_tmp=1.0
		self.min_accuracy=0.55
		self.max_x = 300
		self.max_y = 800
		self.min_x = -300
		self.min_y = -100
		self.data=np.concatenate((x,y), axis=1)
		self.real_points=real_points

	def getCutPoints(self):
		cut_points=np.full((self.max_x-self.min_x, self.max_y-self.min_y), -1.0)
		for p in self.data:
			if p[2]>=self.z_tmp:
				cut_points[(int(p[0])-self.min_x),(int(p[1])-self.min_y)]=p[2]
		return cut_points

	def climb(self):
		best_rate=0.0
		cnt=0
		best_cut_points=None
		while True:
			self.z_tmp=self.z-abs(normalvariate(mu=0.0, sigma=0.05))
			cut_points=self.getCutPoints()
			points=self.getBiggestArea(cut_points)
			rate_tmp=self.rateSolution(points)
			print(self.z_tmp)
			print()
			# plt.contourf( np.arange(-300, 300, 1), np.arange(-100, 800, 1), cut_points.T, 1, cmap=plt.cm.Spectral)
			# plt.show()
			if rate_tmp>best_rate:
				best_rate=rate_tmp
				self.z=self.z_tmp
				best_cut_points=cut_points
				cnt=0
			else:
				cnt+=1
			if cnt>10:
				break
		print('Rate (area) =', best_rate)
		print('Z =', self.z)
		print('Mean =', self.getBiggestArea(best_cut_points)[:,2].mean())
		return self.generateArea(self.getBiggestArea(best_cut_points))

	def rateSolution(self, points):
		mean=self.getRealPointsMean(points)
		print(mean)
		if mean<self.min_accuracy:
			return 0
		else:
			return self.getArea(points)

	def getArea(self, points):
		return len(points)

	def getRealPointsMean(self,points):
		# points = np.array([[-1,-1,0], [-1,0,0], [-1,1,0], [0,-1,0], [0,0,0], [0,1,0], [1,-1,0], [1,0,0], [1,1,0]])
		if points.size==0:
			return 0
		points_to_avg=[]
		for r in self.real_points:
			if (r[0] in points[:,0]) and (r[1] in points[:,1]):
				points_to_avg.append(r)
		# for p in points_to_avg:
			# print(p)
			# input()
		if not points_to_avg:
			return 0
		return np.asarray(points_to_avg)[:,2].mean()

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
		marea=np.array(marea)
		if marea.size==0:
			return marea
		bias=np.full((len(marea),3), [self.min_x, self.min_y, 0.0])
		return np.add(marea,bias)

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

	def generateArea(self, points):
		area=np.full((self.max_x-self.min_x, self.max_y-self.min_y), -1.0)
		for p in points:
			area[(int(p[0])-self.min_x),(int(p[1])-self.min_y)]=p[2]
		return area

