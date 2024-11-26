#medicos.py
from db_connection import connect_to_db

def agregar_medico(nombre, especialidad, telefono):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO Medicos (nombreMedico, especialidad, telefonoMedico)
                VALUES (%s, %s, %s)
            """, (nombre, especialidad, telefono))
            connection.commit()
            print("Médico agregado exitosamente.")
        except Exception as e:
            if "1062" in str(e):
                print(f"Error: El médico {nombre} ya está registrado.")
            else:
                print(f"Error al agregar médico: {e}")
        finally:
            connection.close()



def actualizar_medico(id_medico, nuevo_nombre, nueva_especialidad, nuevo_telefono):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Medicos
                SET nombreMedico = %s, especialidad = %s, telefonoMedico = %s
                WHERE idMedico = %s
            """, (nuevo_nombre, nueva_especialidad, nuevo_telefono, id_medico))
            connection.commit()
            print("Médico actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar médico: {e}")
        finally:
            connection.close()


def ver_detalles_medico():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT idMedico, nombreMedico, especialidad, telefonoMedico
                FROM Medicos
            """)
            print("\nDetalles de Médicos:")
            for row in cursor.fetchall():
                print(f"ID: {row[0]}, Nombre: {row[1]}, Especialidad: {row[2]}, Telefono: {row[3]}")
        except Exception as e:
            print(f"Error al obtener detalles de médicos: {e}")
        finally:
            connection.close()
