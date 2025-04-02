
CREATE DATABASE clientes_db;
USE clientes_db;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL
);


INSERT INTO clientes (nombre, apellido, correo) VALUES
('Juan', 'Pérez', 'juan.perez@email.com'),
('María', 'Gómez', 'maria.gomez@email.com'),
('Carlos', 'Rodríguez', 'carlos.rodriguez@email.com'),
('Ana', 'Fernández', 'ana.fernandez@email.com'),
('Luis', 'Martínez', 'luis.martinez@email.com');

SELECT * FROM clientes





