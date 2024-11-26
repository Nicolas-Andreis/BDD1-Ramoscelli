#reportes.py
from db_connection import connect_to_db

def reporte_turnos():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                SELECT m.nombreMedico, COUNT(t.idTurnos) AS cantidad_turnos
                FROM Medicos m
                LEFT JOIN Turnos t ON m.idMedico = t.idMedico
                GROUP BY m.idMedico
                ORDER BY cantidad_turnos DESC
                LIMIT 3
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            if resultados:
                print("\nReporte de los 3 médicos con más turnos:")
                for medico, cantidad_turnos in resultados:
                    print(f"Médico: {medico}, Turnos: {cantidad_turnos}")
            else:
                print("No se encontraron resultados.")
        except Exception as e:
            print(f"Error al generar el reporte de turnos: {e}")
        finally:
            connection.close()

