\c template1
drop database airData;
create database airData;
\c airdata;
create sequence seq_Aeroprot start 1000 increment 2;
create sequence seq_Vols start 2000 increment 2;
create sequence seq_Compagnie start 3000 increment 2;  
create sequence seq_Avions start 4000 increment 2;

create table Aeroprot(id_areoport varchar primary key default substring('AE' from 1 for 2)||nextval('seq_Aeroprot'),nom varchar,capacite integer);

create table Vols(id_vols varchar default substring('VOLS' from 1 for 2)||nextval('seq_Vols'),depart
varchar,arrivee varchar,nbre_passagers integer,heure_vol time);


create table Compagnie(id_Compagnie varchar primary key default substring('Compagnie' from 1 for 2)||nextval('seq_Compagnie'),nom varchar,nbre_appareil integer);

create table Avions(id_Avions varchar primary key default substring('Avions' from 1 for 2)||nextval('seq_Avions'),modele varchar,nbre_places integer);
