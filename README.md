# Multiplicacion Rusa y Americana
Web que usa metodo de multiplicacion rusa para multiplicar dos numero, generalmnete de muchos digitos, arroja el tiempo que demora en 
ejecutarse en el servidro donde se corre o en local si lo clonas, asi sabes el tiempo que tarda en ejecutarlo tu maquina, usa dos algoritmos el ruso y el amnericano, agrega mas y mandalos en un pull.

# Requisitos

- Necesitas python y flask para ejecutarlo
- MySql y crear una base de datos llamada registro con una tabla llamada registros, aqui te dejo el script.
    
CREATE DATABASE registro;
    
USE registro;

CREATE TABLE registros (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  num1 LONGTEXT,  
  lon1 varchar(10),  
  num2 LONGTEXT,  
  lon2 varchar(10),  
  resultA LONGTEXT,  
  lonResultA varchar(10),  
  resultR LONGTEXT,  
  lonResultR varchar(10),  
  timeA FLOAT,  
  timeR FLOAT  
);  

- Es todo lo que necesitas, recuerda que los tiempos son segun tu maquina ya que aqui se ejecuta todo lo interesante
- Solo clonalo asegurate de tener los requisitos y ejecutalo, recuerda en el archivo main.py
  las lineas 12 y 13 modifia los atributos segun tu usuario y contra en el servidro de MySql
    user="root",
    passwd="",
  En el caso es un ejemplo si tu usuario fuera root y tu passsword fuese una cadena vacia "" lambda.

  by: Safrax

