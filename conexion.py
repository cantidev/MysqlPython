
import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user = "root",
            password= "1234",
            database = "clientes_db"
        )
        if conexion.is_connected():
            return conexion
    except mysql.connector.Error as e:
        print(f'Error de conexion: {e}')

