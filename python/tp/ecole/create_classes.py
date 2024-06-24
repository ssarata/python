import psycopg2
conn=psycopg2.connect('dbname=ecole')
cur=conn.cursor()

class Classes:
	def __init__(self,nom,dure):
		self.nom=nom
		self.dure=dure
	def register_classes(self,libelle,temps):
		liste=[]
		
		liste.append(libelle)
		liste.append(temps)
		return liste
	def delete_classes(self,cour):
		cur.execute("delete from cours where nom=%s",(cour.nom))
		conn.commit()
	
	def add_classes(self,objet):
		cur.execute("insert into cours(nom,dure) values(%s,%s)",(objet.nom,objet.dure))
		conn.commit()
	
		
ob=Classes('bd',2)

