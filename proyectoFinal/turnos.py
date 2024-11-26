#turnos.py
from db_connection import connect_to_db
import datetime

# Función para programar un turno
def programar_turno(fecha, horario, id_paciente, id_medico):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO Turnos (fecha, horario, idPaciente, idMedico)
                VALUES (%s, %s, %s, %s)
            """, (fecha, horario, id_paciente, id_medico))
            connection.commit()
            print("Turno programado exitosamente.")
        except Exception as e:
            if "1062" in str(e):
                print(f"Error: El turno para el médico con ID {id_medico} ya está programado en la fecha {fecha} y horario {horario}.")
            else:
                print(f"Error al programar turno: {e}")
        finally:
            connection.close()


# Función para actualizar un turno
def actualizar_turno(id_turno, nueva_fecha, nuevo_horario):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Turnos
                SET fecha = %s, horario = %s
                WHERE idTurnos = %s
            """, (nueva_fecha, nuevo_horario, id_turno))
            connection.commit()
            print("Turno actualizado exitosamente.")
        except Exception as e:
            # Verificar si el error es un duplicado de clave (código 1062)
            if "1062" in str(e):
                print(f"Error: El turno para el médico ya está programado en la fecha {nueva_fecha} y horario {nuevo_horario}.")
            else:
                print(f"Error al actualizar turno: {e}")
        finally:
            connection.close()


# Función para cancelar un turno
def cancelar_turno(id_turno):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM Turnos WHERE idTurnos = %s
            """, (id_turno,))
            connection.commit()
            print("Turno cancelado exitosamente.")
        except Exception as e:
            print(f"Error al cancelar turno: {e}")
        finally:
            connection.close()

# Función para ver los turnos
def ver_turnos():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT Turnos.idTurnos, Turnos.fecha, Turnos.horario, 
                Pacientes.nombrePaciente AS paciente, Medicos.nombreMedico AS medico
                FROM Turnos
                INNER JOIN Pacientes ON Turnos.idPaciente = Pacientes.idPaciente
                INNER JOIN Medicos ON Turnos.idMedico = Medicos.idMedico
                ORDER BY Turnos.fecha, Turnos.horario  -- Ordenar por fecha y hora
            """)
            for row in cursor.fetchall():
                # Formatear la fecha
                fecha = row[1].strftime("%d/%m/%Y")  # Formato de fecha: dd/mm/yyyy
                
                # Formatear la hora (para el formato 5:02 p. m.)
                hora = (datetime.datetime.min + row[2]).strftime("%I:%M %p")
                hora = hora.lower().replace("am", "a. m.").replace("pm", "p. m.")  # Cambiar a minúsculas y agregar espacio
                
                paciente = row[3]
                medico = row[4]
                print(f"ID Turno: {row[0]}, Fecha: {fecha}, Hora: {hora}, Paciente: {paciente}, Médico: {medico}")
        except Exception as e:
            print(f"Error al obtener turnos: {e}")
        finally:
            connection.close()
