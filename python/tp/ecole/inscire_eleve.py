import psycopg2
conn=psycopg2.connect('dbname=ecole')

import create_classes
cur=conn.cursor()
class Eleve:
	'''def __init__(self):
		return'''
	def __init__(self,nom,prenom,age,idcours):
		super(Eleve, self).__init__()
		#self.idel=idel
		self.__nom=nom
		self.__prenom=prenom
		self.__age=age
		self.__idCours=idcours
	def getNom(self):
		return self.__nom
	
	def getPrenom(self):
		return self.__prenom
	def getAge(self):
		return self.__age
	def getCours(self):
		 return self.__idCours
	def setNom(self,name):
		self.__nom=name
	def setCours(self,idCours):
		 self.__idCours=numEleve
	def setPrenom(self,lastname):
		self.__prenom=lastname
	def setAge(self,old):
		self.__age=old

	def inscrireEleve(self,nom,prenom,age,idcours):
		tab=[]
		tab.append(nom)
		tab.append(prenom)
		tab.append(age)
		tab.append(idcours)
		return tab
		
		
		
	def ajouter_eleve(self,objet):
		print(objet.getCours())
		cur.execute("select idcours from cours where nom=%s",(objet.getCours(),))
		val=cur.fetchone()
		print(val)
		cur.execute("insert into eleve(nom,prenom,age,idcours) values(%s,%s,%s,%s)",(objet.getNom(),objet.getPrenom(),objet.getAge(),val))
		conn.commit()
	
		
'''ob=Eleve('A','A','C','B')
			
tabl=ob.inscrireEleve(nom,prenom,age,idcours)
print(tabl)
el1=Eleve(tabl[0],tabl[1],tabl[2],tabl[3])
ob.ajouter_eleve(el1)

		
#def enregistrer():
		
#enregistrer()
cur.close()
conn.close()'''
