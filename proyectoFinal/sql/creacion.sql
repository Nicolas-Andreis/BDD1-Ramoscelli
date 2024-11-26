-- Eliminar la base de datos si ya existe
DROP DATABASE IF EXISTS SistemaHospital;

-- Creación de la base de datos
CREATE DATABASE SistemaHospital;
USE SistemaHospital;

-- Tabla de Pacientes
CREATE TABLE Pacientes (
    idPaciente INT AUTO_INCREMENT PRIMARY KEY,
    nombrePaciente VARCHAR(100) UNIQUE NOT NULL,
    edad INT NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefonoPaciente VARCHAR(15) NOT NULL
);

-- Tabla de Médicos
CREATE TABLE Medicos (
    idMedico INT AUTO_INCREMENT PRIMARY KEY,
    nombreMedico VARCHAR(100) UNIQUE NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefonoMedico VARCHAR(15) NOT NULL
);

-- Tabla de Turnos
CREATE TABLE Turnos (
    idTurnos INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    horario TIME NOT NULL,
    idPaciente INT NOT NULL,
    idMedico INT NOT NULL,
    UNIQUE (idMedico, fecha, horario), -- Garantiza que un médico no tenga dos turnos a la misma hora
    UNIQUE (idPaciente, fecha, horario), -- Garantiza que un paciente no tenga dos turnos a la misma hora
    FOREIGN KEY (idPaciente) REFERENCES Pacientes(idPaciente) ON DELETE RESTRICT,
    FOREIGN KEY (idMedico) REFERENCES Medicos(idMedico) ON DELETE RESTRICT
);