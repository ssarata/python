class employe:
	def __init__(self,nom,salaire):
		self.nom=nom
		self.salaire=salaire
	def augmenter_salaire(self,newsalaire):
			self.salaire=self.salaire+newsalaire
	def retenue_sur_salaire(self,newsalaire):
			self.salaire=self.salaire-newsalaire
	def afficher(self):
		print(f"{self.nom}  {self.salaire}")
objemp=employe('sankara',600000)
objemp.augmenter_salaire(1)
print(objemp.salaire)
objemp.retenue_sur_salaire(5)
print(objemp.salaire)
objemp.afficher()
