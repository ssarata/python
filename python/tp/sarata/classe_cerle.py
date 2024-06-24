import math
from point import *
class C:
	#pi=3.14
	def __init__(self,a,b,rayon):
		self.x=a
		self.y=b
		self.r=rayon
	def surface(self):
		surface=math.pi*(self.r**2)
		#print(surface)
		return surface
	def perimetre(self):
		perimetre=2*math.pi*self.r
		#print(perimetre)
		return perimetre
	def testAppartenance(self,pt):
		A=math.sqrt((pt.a-self.x)**2+(pt.b-self.y)**2)
		if self.r==A:
			print(f"le pouint A({pt.a},{pt.b}) apparteint au cercle c de centre o({self.x},{self.y}) et de rayon ({self.r})")
		else:
			print(f"le pouint A({pt.a},{pt.b}) n'apparteint pas au cercle c de centre o({self.x},{self.y}) et de rayon ({self.r})")
		

s=C(2,3,5)
p=point(1,1)
#print(s.surface())
#print(s.perimetre())
s.testAppartenance(p)

