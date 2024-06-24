class Personne:
	
	#salaire=5000000
	
	def __init__(self,nom,prenom,datenaissance):
		self.__nomP=nom
		self.__prenomP=prenom
		self.__datenaissanceP=datenaissance
		#self.nomattribut permet de declarer un attribut d'objet(d'instance)
	
	#@classmethod
	#def afficher_nom(a):
		#nom=a('sankara','sarata','01/01/2002')
		#print(nom.nomP)
	#@staticmethod
	#def affichier_prenom():
		#print('pr')
#Personne.afficher_nom()
#Personne.affichier_prenom()
#Personne.afficher_nom()
		

	def getNom(self):
		return self.__nomP
	#pass
	def setPrenom(self,leprenomP):
		if leprenomP.isalpha()==False:
			print('erreur')
		else:
			self.__nomP=leprenomP
	
	
cl=Personne('sankara','sarata','01/01/2002')
print(cl.getNom())
print(cl.setPrenom('toure'))
print(cl.getNom())
print(cl)	
'''
cl=Personne('sankara','sarata','01/01/2002')
print(cl.salaire)
print(cl.nomP)#permet d'afficher la valeur du nomp.pour affichier la valeur de l'attribut on fait nomobjet.nomvariable
print(cl)
cl1=Personne('debebian','chabane','02/02/2002')

print(cl1.nomP)
print(Personne.salaire)
p=cl1.salaire=10000
p1=cl1.lesalaire=15000
print(p)
print(p1)
print(cl.salaire)


@classmethod
	def afficherSalaire(a):
		return a.salaire
	print(Personne.afficherSalaire())
	
	#print('sankara')
	
'''

'''class Client(Personne):
	def __init__(self,nom,prenom,datenaissance,adresse,telephone):
		
		self.adresse=adresse
		self.telephone=telephone
		Personne.__init__(self,nom,prenom,datenaissance)
	
	#pass

cli=Client("akoh","sawana","10/01/2023",'komah',7760)

print(cli.nomP)'''






