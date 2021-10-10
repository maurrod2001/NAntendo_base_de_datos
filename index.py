import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lifegoesonandon",
  database="nantendo"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE tabla_cargo (ID_cargo int AUTO_INCREMENT PRIMARY KEY,"
  +"nombre_cargo VARCHAR(255) not null)")

mycursor.execute("CREATE TABLE tabla_categoria (ID_categoria INT AUTO_INCREMENT PRIMARY KEY,"
  +"nombre_categoria VARCHAR(255) not null)")

mycursor.execute("CREATE TABLE tabla_sede (ID_sede INT AUTO_INCREMENT PRIMARY KEY,"
 +"nombre VARCHAR(255) not null,"
 +"pais VARCHAR(255) not null,"
 +"ciudad VARCHAR(255) not null)")

mycursor.execute("CREATE TABLE tabla_personal (ID_personal int AUTO_INCREMENT PRIMARY KEY,"
 +"nombre VARCHAR(255) not null,"
 +"apellido VARCHAR(255),"
 +"cedula INT not null,"
 +"nacimiento DATE not null)")

mycursor.execute("CREATE TABLE tabla_presupuesto (ID_presupuesto INT PRIMARY KEY,"
 +"encargado int,"
 +"desarrolladores int,"
 +"herramientas int,"
 +"artistas int,"
 +"marketing int,"
 +"innovacion VARCHAR(255))")

mycursor.execute("CREATE TABLE tabla_patrocinadores (ID_patrocinador int AUTO_INCREMENT PRIMARY KEY,"
 +"nombre VARCHAR(255) not null,"
 +"apellido VARCHAR(255),"
 +"dinero_patrocinado int,"
 +"pais VARCHAR(255),"
 +"ciudad VARCHAR(255))")

mycursor.execute("CREATE TABLE tabla_grupo (ID_grupo INT not null PRIMARY KEY,"
 +"ID_personal INT not null," 
 +"ID_cargo INT not null,"
 +"FOREIGN KEY (ID_personal) REFERENCES tabla_personal(ID_personal),"
 +"FOREIGN KEY (ID_cargo) REFERENCES tabla_cargo(ID_cargo))")


mycursor.execute("CREATE TABLE tabla_proyectos (ID_proyecto int AUTO_INCREMENT PRIMARY KEY,"
 +"nombre_proyecto VARCHAR(255) not null,"
 +"ID_encargado INT,"
 +"ID_grupo INT,"
 +"ID_sede INT,"
 +"ID_patrocinador INT,"
 +"ID_presupuesto INT,"
 +"FOREIGN KEY (ID_encargado) REFERENCES tabla_personal(ID_personal),"
 +"FOREIGN KEY (ID_grupo) REFERENCES tabla_grupo(ID_grupo),"
 +"FOREIGN KEY (ID_patrocinador) REFERENCES tabla_patrocinadores(ID_patrocinador),"
 +"FOREIGN KEY (ID_presupuesto) REFERENCES tabla_presupuesto(ID_presupuesto),"
 +"FOREIGN KEY (ID_sede) REFERENCES tabla_sede(ID_sede))")

