\c template1
drop database ecole;
create database ecole;
\c ecole
create sequence seq_note;
create table eleves(id_eleve integer primary key,nom varchar,prenom varchar,age integer);
create table note(idnote integer primary key default nextval ('seq_note'),valeur integer,id_eleve integer references eleves);
