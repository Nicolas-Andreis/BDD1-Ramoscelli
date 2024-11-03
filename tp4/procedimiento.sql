DELIMITER //
CREATE PROCEDURE AsignarRecursosAProyectos()
BEGIN
    DECLARE ProyectoId INT;
    DECLARE RecursosNecesarios INT;
    DECLARE RecursosAsignados INT;
    DECLARE EstadoProyecto VARCHAR(20);
    DECLARE CantidadDisponible INT;
    DECLARE done INT DEFAULT FALSE;

    -- Cursor para seleccionar proyectos en estado 'Pendiente', ordenados por 'RecursosNecesarios' de mayor a menor
    DECLARE cursor_proyectos CURSOR FOR
        SELECT ProyectoId, RecursosNecesarios, RecursosAsignados, Estado
        FROM Proyectos
        WHERE Estado = 'Pendiente'
        ORDER BY RecursosNecesarios DESC;

    -- Handler para finalizar el cursor cuando no haya más filas
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Abrir el cursor
    OPEN cursor_proyectos;

    -- Obtener el primer proyecto pendiente
    FETCH cursor_proyectos INTO ProyectoId, RecursosNecesarios, RecursosAsignados, EstadoProyecto;

    WHILE NOT done DO
        BEGIN
            -- Verificar si hay suficientes recursos disponibles
            SELECT SUM(CantidadDisponible) INTO CantidadDisponible
            FROM RecursosDisponibles
            WHERE CantidadDisponible >= RecursosNecesarios;

            IF CantidadDisponible IS NOT NULL AND CantidadDisponible >= RecursosNecesarios THEN
                -- Asignar recursos al proyecto
                UPDATE Proyectos
                SET RecursosAsignados = RecursosAsignados + RecursosNecesarios,
                    Estado = 'En Curso'
                WHERE ProyectoId = ProyectoId;

                -- Decrementar la cantidad disponible de recursos
                UPDATE RecursosDisponibles
                SET CantidadDisponible = CantidadDisponible - RecursosNecesarios
                WHERE CantidadDisponible >= RecursosNecesarios
                LIMIT 1;  -- Decrementar solo un recurso
            END IF;

            -- Obtener el siguiente proyecto pendiente
            FETCH cursor_proyectos INTO ProyectoId, RecursosNecesarios, RecursosAsignados, EstadoProyecto;
        END;
    END WHILE;

    -- Cerrar el cursor
    CLOSE cursor_proyectos;
END//
DELIMITER ;