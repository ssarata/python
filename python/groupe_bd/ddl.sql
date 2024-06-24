/*Un type composite représente la structure d'une ligne ou d'un enregistrement ; il est en essence une simple liste de noms de champs et de leur types de données. PostgreSQL™ autorise l'utilisation de types composite identiques de plusieurs façons à l'utilisation des types simples. Par exemple, une colonne d'une table peut être déclarée comme étant de type composite.
syntaxe pour declerer un type complexe
CREATE TYPE name AS
    ( [ attribute_name data_type [ COLLATE collation ] [, ... ] ] )*/
--create table personne(idpersonne integer primary key,nom varchar,prenom varchar);
--create table personne(idpersonne integer primary key,nom varchar,prenom varchar);
create type personne as (nom varchar,prenom varchar);
create table client(identifiant personne,adresse varchar);


/*Pour faire l insertion dans une table ayant pour colonne un type composite on ouvre les parenthèses pour saisir les champs corresppondant et séparez-les par des virgules. Vous pouvez placer des guillemets doubles autour de chaque valeur de champ et vous devez le faire si elle contient des virgules ou des parenthèses .

Pour mettre un attribut la valeur null on met les parenthèses du type composite en guillemets unique et guillemets doubles  pour la valeur nulle et les champs type chaine et 
Pour mettre un attribut vide on met les parenthèses du type composite en guillemets unique et virgule */







--insert into client values(('sankara','sarata'),'sokode');
--insert into client values('("akoh",)','sokode'); enregistrement d'un client ayant pour prenom vide
--insert into client values('("beveri","")','sokode');enregistrement d'un client ayant pour prenom null




--La syntaxe dexpression ROW pourrait aussi être utilisée pour construire des valeurs composites.Avec le mot clé row  nous navons pas à nous besoin des multiples couches de guillemets


--insert into client values (identifiant) = ROW('zina','','sokode');
--Pour accéder à un champ d'une colonne composite on ecrit le nom de colonne point le nom  du champ ou (table_name.colonne_composite_name.nom_champ).notons bien le nom de colonne doit etre toujours entre parenthese .exemple
select (identifiant).nom from client;






























