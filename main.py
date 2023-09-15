from flask import Flask, redirect, request, render_template
import time

import mysql.connector

app = Flask(__name__)

prog = Flask(__name__)
conDB = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    db="registro"
)
miCursor = conDB.cursor()

def rusa(a, b):
    a = int(a)
    b = int(b)
    resultado = 0
    while(a > 0):
        if(a % 2 != 0):
            resultado += b
        b += b
        a //= 2
    return resultado


#americana     
    
def americana(A, B):
    A_str = str(A)
    B_str = str(B)
    
    len_A = len(A_str)
    len_B = len(B_str)
    
    # Definimos una matriz de 2 dimensiones para los productos parciales
    productos_parciales = [[0] * (len_B + len_A) for _ in range(len_A)]
    
    for i in range(len_A):
        for j in range(len_B):
            producto = int(A_str[i]) * int(B_str[j])
            productos_parciales[i][i + j] = producto
    
    # Realiza la suma de los productos parciales y almacena el acarreo
    resultado = [0] * (len_A + len_B)
    for i in range(len_A):
        for j in range(len_A + len_B):
            resultado[j] += productos_parciales[i][j]
    
    # Realiza el acarreo hacia arriba en el resultado
    for i in range(len_A + len_B - 1, 0, -1):
        carry = resultado[i] // 10
        resultado[i] %= 10
        resultado[i - 1] += carry
        
    # Convierte el resultado en un número entero int
    resultado_entero = int(''.join(map(str, resultado)).rstrip('0'))
    
    return resultado_entero



@app.route("/", methods=["GET", "POST"])
def index():
    resultadoRusa = ""
    resultadoAmericana = ""
    tiempo = 0
    tiempo2 = 0
    if request.method == "POST":
        numero11 = int(request.form.get("numero1"))
        numero22 = int(request.form.get("numero2"))
        numero1 = str(numero11)
        numero2 = str(numero22) 
        inicio = time.time_ns() 
        resultadoRusa = str(rusa(numero11, numero22))
        final = time.time_ns()
        inicio2 = time.time_ns() 
        resultadoAmericana = str(americana(numero11, numero22))
        final2 = time.time_ns()
        tiempo2 = final2 - inicio2
        tiempo = final - inicio
        sql = f"INSERT INTO registros(num1, num2, resultA, resultR, timeA, timeR) VALUES('{numero1}', '{numero2}', '{resultadoAmericana}', '{resultadoRusa}', {tiempo}, {tiempo2});"
        miCursor.execute(sql)
        conDB.commit()
        resultadosql = miCursor.fetchall()

        
    return render_template("index.html", resultadoAmericana=resultadoAmericana, resultadoRusa=resultadoRusa, tiempo=tiempo, tiempo2=tiempo2)

@app.route("/registros", methods=["GET", "POST"])
def registros():
     # Consulta todos los registros de la tabla
    sql = "SELECT * FROM registros;"
    miCursor.execute(sql)
    registros = miCursor.fetchall()

    return render_template("registros.html", registros=registros)

@app.route("/borrar_registros", methods=["POST"])
def borrarRegistros():
    print("entre en borrar")
    try:
        sql = "TRUNCATE TABLE registros;"
        miCursor.execute(sql)
        conDB.commit()
        print("Registros eliminados con éxito")
    except Exception as e:
        print("Error al borrar registros:", e)
    return redirect("/registros")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4001)
