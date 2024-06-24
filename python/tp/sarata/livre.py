class livre:
	def __init__(self,titre,auteur,prix,nombrepages):
		self.titre=titre
		self.auteur=auteur
		self.prix=prix
		self.nombrespages=nombrepages
	def modifier_prix(self,prix):
		self.prix=prix
	def afficher_details(self):
		print(f"{self.titre},{self.auteur},{self.prix},{self.nombrespages}")
		
		
		
objet_livre=livre('bd','sankara',2000,50)
print(objet_livre.prix)

objet_livre.modifier_prix(5000)
print(objet_livre.prix)
objet_livre.afficher_details()
