#busquedas.py 
from db_connection import connect_to_db

def buscar_paciente(atributo, termino):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            
            if atributo == "idPaciente":  # Si el atributo es un ID, usamos comparación exacta
                query = f"SELECT * FROM Pacientes WHERE {atributo} = %s"
                cursor.execute(query, (termino,))
            else:  # Para otros atributos, seguimos usando LIKE
                query = f"SELECT * FROM Pacientes WHERE LOWER({atributo}) LIKE %s"
                cursor.execute(query, (f"%{termino.lower()}%",))
            
            resultados = cursor.fetchall()
            if resultados:
                for paciente in resultados:
                    print(paciente)
            else:
                print("No se encontraron pacientes con los criterios especificados.")
        except Exception as e:
            print(f"Error en la búsqueda de pacientes: {e}")
        finally:
            connection.close()

def buscar_medico(atributo, termino):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            
            if atributo == "idMedico":  # Si el atributo es un ID, usamos comparación exacta
                query = f"SELECT * FROM Medicos WHERE {atributo} = %s"
                cursor.execute(query, (termino,))
            else:  # Para otros atributos, seguimos usando LIKE
                query = f"SELECT * FROM Medicos WHERE LOWER({atributo}) LIKE %s"
                cursor.execute(query, (f"%{termino.lower()}%",))
            
            resultados = cursor.fetchall()
            if resultados:
                for medico in resultados:
                    print(medico)
            else:
                print("No se encontraron médicos con los criterios especificados.")
        except Exception as e:
            print(f"Error en la búsqueda de médicos: {e}")
        finally:
            connection.close()

