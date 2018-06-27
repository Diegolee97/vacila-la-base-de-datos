from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE camionero 
           (rut interger ,id serial PRIMARY KEY, nombre varchar(100), contacto interger, salario interger,
           domicilio varchar(100), tipo_licencia varchar(10));
"""

cur.execute(sql)


sql ="""
CREATE TABLE camion 
           (id_camion serial PRIMARY KEY, matricula varchar(40), idcamionero interger, modelo varchar(40), 
           tipo varchar(40), Capacidad interger, cap_especiales varchar(250), id_paquete interger);
"""


cur.execute(sql)

sql ="""
CREATE TABLE paquete
           (id_paquete serial PRIMARY KEY, tamaño interger, descripcion text, destinatario, text, codigo_postal interger,
           f_envio timestamp, direccion_destino varchar(100), necesidades_esp varchar(250), id_camion interger);
"""

cur.execute(sql)

sql ="""
CREATE TABLE ciudad
           (codigo_ciudad serial PRIMARY KEY, nombre varchar(100), codigo_postal interger, f_llegada timestamp);
"""

cur.execute(sql)




conn.commit()
cur.close()
conn.close()
