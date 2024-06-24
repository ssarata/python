import inscire_eleve
import create_classes
class Test:
	
	
	
	
	def engeristrerCours():
		libelle=input("saisir le nom du cours: ")
		temps=input("saisir la dure du cours: ")
		ob=create_classes.Classes('bd',4)
		classes1=ob.register_classes(libelle,temps)
		oject_classes=create_classes.Classes(classes1[0],classes1[1])
		oject_classes.add_classes(oject_classes)
	#engeristrerCours()	
	def supprimer():
		libelle=input("saisir le nom du cours: ")
		ob=create_classes.Classes('bd',4)
		obj1=ob.delete_classes(libelle)
	
	
	def enregistrer():
		nom=input("saisir le nom de l'élève:  ")
		prenom=(input("saisir le prenom de l'élève:  "))
		age=int(input("saisir lâge de l'élève superieur à 16:	"))
		while (age<16):
			age=int(input("Erreur!!ressaisir lâge de l'élève superieur à 16:  "))
		idcours=(input("saisir le nom du cours "))
		ob=inscire_eleve.Eleve('A','A','C','B')
			
		tabl=ob.inscrireEleve(nom,prenom,age,idcours)
		print(tabl)
		el1=inscire_eleve.Eleve(tabl[0],tabl[1],tabl[2],tabl[3])
		ob.ajouter_eleve(el1)
		

	#enregistrer()
	
	
def main():
	print('1 enregistrer un élève')
	print('2 enregistrer un élève')
	print('3 supprimer un cours')
	print('4 renvoyer un élève')
	print('5 modifier un élève')
	print('lister les élèves d un cours')
	choix=input('enter votre choix: ')
	while choix!='1' and choix!='2' and choix!='3':
		choix=input('enter votre choix: ')
	if choix=='1':
		Test.enregistrer()
		choix=input("saisir oui pour continuer et non pour quitte")
		while choix!='oui' and choix!='non':
			choix=input("saisir oui pour continuer et non pour quitte: ")
		while  choix=='oui':
			Test.enregistrer()
			choix=input("saisir oui pour continuer et non pour quitte: ")
			while choix!='oui' and choix!='non':
				choix=input("saisir oui pour continuer et non pour quitte  :")
		else:
			print("ok")
			
				 
	elif choix=='2':
		Test.engeristrerCours()
		choix=input("saisir oui pour continuer et non pour quitte")
		while choix!='oui' and choix!='non':
			choix=input("saisir oui pour continuer et non pour quitte: ")
		while  choix=='oui':
			Test.engeristrerCours()
			choix=input("saisir oui pour continuer et non pour quitte: ")
			while choix!='oui' and choix!='non':
				choix=input("saisir oui pour continuer et non pour quitte  :")
		else:
			print("ok")
	elif choix=='3':
		 Test.supprimer()
			
main()
	
	
