#pacientes.py
from db_connection import connect_to_db

from db_connection import connect_to_db

def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    direccion = input("Ingrese la dirección del paciente: ")
    telefono = input("Ingrese el teléfono del paciente: ")
    
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO Pacientes (nombrePaciente, edad, direccion, telefonoPaciente)
                VALUES (%s, %s, %s, %s)
            """, (nombre, edad, direccion, telefono))
            connection.commit()
            print("Paciente registrado exitosamente.")
        except Exception as e:
            # Verificar si el error es un duplicado de clave (código 1062)
            if "1062" in str(e):
                print(f"Error: El paciente {nombre} ya está registrado.")
            else:
                print(f"Error al registrar paciente: {e}")
        finally:
            connection.close()


def ver_pacientes():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Pacientes")
            pacientes = cursor.fetchall()
            for paciente in pacientes:
                print(paciente)
        except Exception as e:
            print(f"Error al obtener pacientes: {e}")
        finally:
            connection.close()

def actualizar_paciente():
    id_paciente = int(input("Ingrese el ID del paciente a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del paciente: ")
    edad = int(input("Ingrese la nueva edad del paciente: "))
    direccion = input("Ingrese la nueva dirección del paciente: ")
    telefono = input("Ingrese el nuevo teléfono del paciente: ")
    
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Pacientes
                SET nombrePaciente = %s, edad = %s, direccion = %s, telefonoPaciente = %s
                WHERE idPaciente = %s
            """, (nombre, edad, direccion, telefono, id_paciente))
            connection.commit()
            print("Paciente actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar paciente: {e}")
        finally:
            connection.close()

def eliminar_paciente():
    id_paciente = int(input("Ingrese el ID del paciente a eliminar: "))
    
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Pacientes WHERE idPaciente = %s", (id_paciente,))
            connection.commit()
            print("Paciente eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar paciente: {e}")
        finally:
            connection.close()
