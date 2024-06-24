from openpyxl import load_workbook
import psycopg2
conn=psycopg2.connect('dbname=ecole')
cur=conn.cursor()

objet = load_workbook(filename = 'eleves.xlsx')
note=objet['Notes']
eleves=objet['Eleves']

val_notes=note.values
val_eleves=eleves.values
def eleve(val_eleves):
	print(val_eleves)
	tab=[]
	for i in val_eleves:
		print(i)
		tab.append(i)

	for j in range(len(tab)):
		if j!=0:
			tup=tab[j]
			cur.execute('insert into eleves values(%s,%s,%s)',(tup[0],tup[1],tup[2]))
			conn.commit()
#eleve(val_eleves)
def notes(val_notes):
	tabs=[]	
	for i in val_notes:
		tabs.append(i)
	for j in range(len(tabs)):
		if j!=0:
			tuples=tabs[j]
			cur.execute('select id_eleve from eleves where nom=%s and prenom=%s',(tuples[0],tuples[1]))
			ideleve=cur.fetchone()[0]
			print(ideleve)
			cur.execute('insert into note(valeur,id_eleve) values(%s,%s)',(tuples[2],ideleve))
			conn.commit()

#notes(val_notes)
cur.close()
conn.close()

