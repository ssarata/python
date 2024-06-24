class Voiture:
	def __init__(self,marque,capacite,puissance):
		self.marque=marque
		self.capacite=capacite
		self.puissance=puissance
	def afficher_infos(self):
		print(f'marque: {self.marque}\ncapacite: {self.capacite}\npuissance:{self.puissance}')
	def get_marque(self):
		return self.marque
	def set_marque(self,newmarque):
		self.marque=newmarque
	def get_capacite(self):
		return self.capacite
	def set_capacite(self,newcapacite):
		self.capacite=newcapacite
		
	def get_puissance(self):
		return self.puissance
	def set_puissance(self,newpuissance):
		self.puissance=newpuissance
		

class VoitureHybride(Voiture):
	def __init__(self,marque,capacite,puissance,temps):
		self.temps=temps
		Voiture.__init__(self,marque,capacite,puissance)
		
	def afficher_hybride(self):
		print(f'temps dautonomie {self.temps}')
	def get_temps(self):
		return self.temps
	def set_temps(self,newtemps):
		self.temps=newtemps
		
v1=Voiture('rav4',4,2)
v1.afficher_infos()
print(v1.get_marque())
v1.set_marque(10)

print(v1.get_capacite())

v1.set_capacite(10)
v1.get_puissance()
v1.set_puissance(10)
v1.afficher_infos()

vh1=VoitureHybride('landcruser',20,'20kw','20')
vh1.afficher_hybride()

vh1.get_temps()

vh1.set_temps(5)
vh1.afficher_hybride()








