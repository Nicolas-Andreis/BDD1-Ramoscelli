INSERT INTO Proyectos (NombreProyecto, RecursosNecesarios, RecursosAsignados, Estado)
VALUES 
    ('Proyecto A', 10, 0, 'Pendiente'),
    ('Proyecto B', 5, 0, 'Pendiente'),
    ('Proyecto C', 15, 0, 'Pendiente'),
    ('Proyecto D', 8, 0, 'Pendiente'),
    ('Proyecto E', 3, 0, 'Pendiente');

-- Inserción de datos en la tabla RecursosDisponibles
INSERT INTO RecursosDisponibles (TipoRecurso, CantidadDisponible)
VALUES
    ('Recurso X', 20),
    ('Recurso Y', 10),
    ('Recurso Z', 5);
