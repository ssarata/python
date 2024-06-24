import psycopg2
conn=psycopg2.connect('dbname=GestionLivre')
cur=conn.cursor()
class Book:#declaration de la classe Book
	def __init__(self,titre=" ",auteur=" ",category=" "):#definition du constructeur
		self.titre=titre
		self.auteur=auteur
		self.category=category
	@staticmethod
	def create_table():#declaration d'une methode de classe qui permet de creer les tables
		cur.execute("create sequence se_auteur")
		cur.execute("create sequence se_book")
		cur.execute("create table auteur(idAuteur integer primary key default nextval('se_auteur'),nom varchar)")
		cur.execute("create table book(idBook integer primary key default nextval('se_book'),title varchar,categorie varchar,idAuteur integer references auteur)")

	def add_book(self,b1):#declaration d'une methode d'instance qui permet d'inserer les objets dans la base de donnée
		cur.execute("insert into auteur(nom) values(%s)",(b1.auteur,))
		cur.execute("select idAuteur from auteur where nom=%s",(b1.auteur,))
		aut=cur.fetchone()
		aut=aut[0]
		#print(aut)
		cur.execute("insert into book(title,categorie,idAuteur) values(%s,%s,%s)",(b1.titre,b1.category,aut))
		
	@staticmethod
	def display():#declaration d'une mehode de classe qui permet de d'afficher la liste des livres
		tabs=[]
		cur.execute("select title,nom,categorie from book,auteur where auteur.idAuteur=book.idAuteur")
		liste=cur.fetchall()
		for i in liste:
			ob=Book(i[0],i[1],i[2])
			resultat=(ob.titre,ob.auteur,ob.category)
			tabs.append(resultat)
		print(tabs)
	
	def get_titre(self):#une fonction getters qui permet de recuperer le titre
		return self.titre
		
	def get_auteur(self):#une fonction getters qui permet de recuperer l'auteur
		return self.auteur
		
	def get_category(self):#une fonction getters qui permet de recuperer la category
		return self.category
		
	def set_titre(self,titre):#une methode setter qui permet de modifier le titre
		 self.titre=titre
		 
	def set_auteur(self,auteur):#une methode setter qui permet de modifier l'auteur
		 self.auteur=auteur
		
	def set_category(self,category):#une methode setter qui permet de modifier la category
		 self.category=category
		
	def get_livre(self,idlivre):#une methode d'instance qui permet de recuper les informations d'un livre
	
		cur.execute("select title,nom,categorie,book.idAuteur,idBook from book,auteur where auteur.idAuteur=book.idAuteur")
		livre=cur.fetchall()[0]
		return livre
	
	def update(self,ob,idlivre,idauteur):#une methode qui permet de mettre a jour les informations dun livre
		print(self.titre)
		print(ob.titre)
		if self.titre!=ob.titre:
		 	cur.execute("update book set title=%s where idBook=%s",(ob.titre,idlivre,))
		 	conn.commit()
		if self.auteur!=ob.auteur:
			cur.execute("update auteur set nom=%s where idAuteur=%s",(ob.auteur,idauteur,))
			conn.commit()
		if self.category!=ob.category:
			cur.execute("update book set categorie=%s where idBook=%s",(ob.category,idlivre,))
			conn.commit()
	def delete(self,idlivre):#une methode qui permet de supprimer les informations dun livre
		cur.execute("delete from book where idBook=%s",(idlivre,))
		conn.commit()



book = Book()#creation d'un objet book
Book.create_table()
b1=Book('bd','koumai','l2')#creation d'un objet book
b3=Book('anglais','akoh','l2')#creation d'un objet book
b2=Book('python','toure','l3')#creation d'un objet book
book.add_book(b1)#insertion de l'objet b1 dans la base
book.add_book(b2)#insertion de l'objet b2 dans la base
book.add_book(b3)#insertion de l'objet b3 dans la base
conn.commit()
print(b1.get_titre())
print(b1.get_category())
print(b1.get_auteur())
livre=b1.get_livre(4)
print(livre)
oldb1=Book(livre[0],livre[1],livre[2])#creation d'un objet avec les informations du livre recuperer dans la base de donnée
oldb1.set_auteur('sankara')#modification de son auteur
oldb1.set_category('l2')#modification de sa category
oldb1.set_titre('bd')#modification de son titre
print(oldb1.auteur,oldb1.titre,oldb1.category)
newb1=Book(oldb1.get_titre(),oldb1.get_auteur(),oldb1.get_category())#creation d'un nouveau objet avec les valeurs modifiées
newb1=Book('pyton','toure','l3')
b1.update(oldb1,livre[3],livre[4])#mis a jour du livre

Book.display()
book.delete(3)

