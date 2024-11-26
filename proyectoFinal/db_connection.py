#db_connection
import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambiar por tu usuario
            password="root",  # Cambiar por tu contraseña
            database="SistemaHospital"
        )
        return connection
    except Error as e:
        print(f"Error conectando a la base de datos: {e}")
        return None
