def menu_medicos():
    while True:
        print("\n---- Gestión de Médicos ----")
        print("1. Agregar médico")
        print("2. Ver detalles de médicos")
        print("3. Actualizar médico")
        print("4. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del médico: ")
            especialidad = input("Ingrese la especialidad del médico: ")
            telefono = input("Ingrese el teléfono del médico: ")
            agregar_medico(nombre, especialidad, telefono)
        elif opcion == "2":
            ver_detalles_medico()
        elif opcion == "3":
            id_medico = int(input("Ingrese el ID del médico a actualizar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del médico: ")
            nueva_especialidad = input("Ingrese la nueva especialidad del médico: ")
            nuevo_telefono = input("Ingrese el nuevo telefono del médico: ")
            actualizar_medico(id_medico, nuevo_nombre, nueva_especialidad, nuevo_telefono)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")