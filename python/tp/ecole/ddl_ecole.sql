\c template1
drop database ecole;
create database ecole;
\c ecole
create sequence seq_cours start 1000;
create sequence seq_eleve start 1000;
create table cours(idcours integer default nextval('seq_cours') primary key,
	nom varchar,
	dure integer);

create table eleve(ideleve integer default nextval('seq_eleve') primary key,
	nom varchar
	,prenom varchar
	,age integer,
	idcours integer references cours);
