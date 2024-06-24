class connexion:
	
	def connect(nom):
		import psycopg2
		base='dbname='
		name=nom
		conn=psycopg2.connect(base+nom)
		cur=conn.cursor()
		cur.execute("select * from eleve")
		var=cur.fetchall()
		print(var)
		
	connect('ecole')
	
