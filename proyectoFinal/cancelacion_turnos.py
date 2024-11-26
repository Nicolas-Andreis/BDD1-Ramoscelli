#cancelacion_turnos.py
from db_connection import connect_to_db


def cancelar_turno_por_fecha(fecha):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM Turnos WHERE fecha = %s"
            cursor.execute(query, (fecha,))
            connection.commit()
            print(f"Turnos para la fecha {fecha} han sido cancelados.")
        except Exception as e:
            print(f"Error al cancelar los turnos: {e}")
        finally:
            connection.close()

def cancelar_turno_por_medico(medico_id):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM Turnos WHERE idMedico = %s"
            cursor.execute(query, (medico_id,))
            connection.commit()
            print(f"Turnos para el médico con ID {medico_id} han sido cancelados.")
        except Exception as e:
            print(f"Error al cancelar los turnos: {e}")
        finally:
            connection.close()
