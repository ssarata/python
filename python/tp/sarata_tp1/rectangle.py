class Rectangle:
	def __init__(self,longu,lar):
		self.longueur=longu
		self.largeur=lar
	def perimetre(self):
		peri=self.longueur+self.largeur
		return peri
	def surface(self):
		
		aire=self.longueur*self.largeur
		return aire
	def setrec(self):
		
		return self.longueur
	def getrec(self,l):
		self.longueur=l
	def setlar(self):
		
		return self.largeur
	def getlar(self,l):
		self.largeur=l
p=Rectangle(2,4)
'''print(p.perimetre())
print(p.surface())				
print(p.setrec())
print(p.getrec(9))
print(p.setrec())
print(p.setlar())
print(p.getlar(9))
print(p.setlar())'''


class parallelopipede(Rectangle):
	def __init__(self,longu,lar,h):
		self.hauteur=h
		Rectangle.__init__(self,longu,lar)
		
	def volume(self):
		v=self.longueur*self.largeur*self.hauteur
		print(v)
p1=parallelopipede(2,4,2)
p1.volume()
print(p1.perimetre())











