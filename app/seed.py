from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

# Camioneros

sql ="""
insert into camionero (rut,nombre,contacto,salario,domicilio,tipo_licencia) values ('12497520','Ramon Valdes', '56947813549','430000',
'Los peces 204, SextaAnormal','A4'),('8612345','Roberto Gomez','56943315786','500000','Perrudos 1313,Vaticano','A5'),('9335142',
'Carlos Villasola','56984651244','520000','Pantuflas 420, La Cisterna','A4');
"""

cur.execute(sql)

# Camiones

sql ="""
insert into camion (matricula,modelo,tipo,capacidad,cap_especiales) values ('46 58 JP','Bulbo FS','Camion araucario','36','Refrigeracion'),
('89 69 CG','Mock 205','Camion Largo','48','null');
"""

cur.execute(sql)

# Paquetes

sql ="""
insert into paquete (tamaño,descripcion,codigo_postal,f_envio,destinatario,direccion_destino,necesidades_esp) values('6','Paquete plano, largo y ancho',
'99877',now(),'Manolo Amanecer','Los loros 1010, Molbo','Refrigeracion'),('1.5','Paquete cuadrado con forma de caja',now(),'Cornolio Gutierrez','Sucasa 4412,Cerritos','null'),
('3','Paquete alto con base pequeña, color blanco',now(),'Elmer Curio','Fachito 1973, Valpoloiso','Refrigeracion');
"""
cur.execute(sql)

# Ciudades

sql ="""
insert into ciudad (nombre,region) values('Cañulefioniso','RM'),('Punta del Cerro','V');
"""

cur.execute(sql)



conn.commit()
cur.close()
conn.close()
