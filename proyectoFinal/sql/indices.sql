-- Creación de índices para optimizar las consultas frecuentes

-- Índice para el campo nombrePaciente en la tabla Pacientes
CREATE INDEX idx_nombrePaciente ON Pacientes (nombrePaciente);

-- Índice para los campos especialidad y telefonoMedico en la tabla Medicos
CREATE INDEX idx_especialidad ON Medicos (especialidad);
CREATE INDEX idx_telefonoMedico ON Medicos (telefonoMedico);

-- Índice para los campos idPaciente y idMedico en la tabla Turnos
CREATE INDEX idx_idPaciente ON Turnos (idPaciente);
CREATE INDEX idx_idMedico ON Turnos (idMedico);

-- Índice compuesto para los campos fecha y horario en la tabla Turnos
CREATE INDEX idx_fecha_horario ON Turnos (fecha, horario);