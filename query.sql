-- First Table
-- CREATE TABLE "Registros"(
--     id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
--     email TEXT NOT NULL,
--     contrasena TEXT NOT NULL
-- );
-- DELETE FROM Registros WHERE email = "oscarariasodag2000@gmail.com";
-- Second Table
-- CREATE TABLE "Suscripcion"(
--     id_plan INTEGER PRIMARY KEY AUTOINCREMENT,
--     tipo_plan TEXT NOT NULL,
--     precio REAL NOT NULL
-- );

-- DROP TABLE Registros;

-- CREATE TABLE "Usuarios_Suscripcion" (
--     id_usuario_suscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
--     id_registro INTEGER NOT NULL,
--     id_suscripcion INTEGER NOT NULL,
--     FOREIGN KEY(id_registro) REFERENCES Registros(id_registro),
--     FOREIGN KEY(id_suscripcion) REFERENCES Suscripcion(id_plan)
-- );

-- DROP TABLE Usuarios_Suscripcion;






-- Third Table
-- CREATE TABLE "Pais"(
--     id_pais INTEGER PRIMARY KEY,
--     nombre_pais TEXT NOT NULL
-- );

-- DROP TABLE Pais;

-- ALTER TABLE Ciudad DROP CONSTRAINT
-- codigo_pais;

-- UPDATE TABLE Pais
-- id_pais INTEGER AUTOINCREMENT PRIMARY KEY









-- INSERT INTO Registros(email, contrasena) VALUES("oscarariasodag2000@gmail.com", "456odag");





-- CREATE TABLE "Tipo_Transaccion"(
--     codigo_transaccion INTEGER PRIMARY KEY,
--     descripcion TEXT NOT NULL
-- );

-- UPDATE TABLE Tipo_Transaccion
-- codigo_transaccion INTEGER AUTOINCREMENT PRIMARY KEY

-- CREATE TABLE "Tipo_Inmueble"(
--     código_tipo INTEGER PRIMARY KEY,
--     descripcion TEXT NOT NULL
-- );

-- UPDATE TABLE Tipo_Inmueble
-- codigo_tipo INTEGER AUTOINCREMENT PRIMARY KEY

-- CREATE TABLE "Ciudad"(
--     código_ciudad INTEGER PRIMARY KEY,
--     nombre TEXT NOT NULL
-- );

-- UPDATE TABLE Ciudad
-- codigo_ciudad INTEGER AUTOINCREMENT PRIMARY KEY

-- CREATE TABLE "Usuarios_Suscripcion"(
--     id_usuario_suscripcion INTEGER PRIMARY KEY,
--     id_registro INTEGER NOT NULL,
--     id_suscripcion INTEGER NOT NULL,
--     FOREIGN KEY(id_registro) REFERENCES Registros(id_registro)
--     FOREIGN KEY(id_suscripcion) REFERENCES Suscripcion(id_plan)
-- );




-- UPDATE TABLE Usuarios_Suscripcion
-- id_usuario_suscripcion INTEGER AUTOINCREMENT PRIMARY KEY
INSERT INTO Ciudad(nombre) VALUES("Managua");
-- CREATE TABLE "Usuarios"(
--     codigo_usuario INTEGER PRIMARY KEY,
--     nombre_completo TEXT NOT NULL,
--     telefono INTEGER NOT NULL,
--     id_registro INTEGER,
--     domicilio TEXT NOT NULL,
--     codigo_ciudad INTEGER,
--     FOREIGN KEY(id_registro) REFERENCES Registros(id_registro)
--     FOREIGN KEY(codigo_ciudad) REFERENCES Ciudad(codigo_ciudad)
-- );
-- DROP TABLE Usuarios;



-- UPDATE TABLE Usuarios
-- codigo_usuario INTEGER AUTOINCREMENT PRIMARY KEY

-- CREATE TABLE "Propiedades"(
--     codigo_propiedad INTEGER PRIMARY KEY AUTOINCREMENT,
--     direccion TEXT NOT NULL,   
--     precio REAL NOT NULL,
--     moneda TEXT NOT NULL,
--     codigo_ciudad INTEGER,
--     tipo_inmueble INTEGER,
--     codigo_usuario_suscripcion INTEGER,
--     estado TEXT NOT NULL,
--     FOREIGN KEY(codigo_ciudad) REFERENCES Ciudad(codigo_ciudad),
--     FOREIGN KEY(tipo_inmueble) REFERENCES Tipo_Inmueble(codigo_tipo),
--     FOREIGN KEY(codigo_usuario_suscripcion) REFERENCES Usuarios_Suscripcion(id_usuario_suscripcion)
-- );
-- DROP TABLE Propiedades;


-- UPDATE TABLE Propiedades
-- codigo_propiedad INTEGER AUTOINCREMENT PRIMARY KEY

-- CREATE TABLE "Transacciones"(
--     id_transacciones INTEGER PRIMARY KEY,
--     codigo_tipo_transaccion INTEGER,
--     codigo_propiedad INTEGER,
--     codigo_interesado INTEGER,
--     FOREIGN KEY(codigo_tipo_transaccion) REFERENCES Tipo_Transaccion(codigo_transaccion)
--     FOREIGN KEY(codigo_propiedad) REFERENCES Propiedades(codigo_propiedad)
--     FOREIGN KEY(codigo_interesado) REFERENCES Usuarios(codigo_usuario)
-- );

-- UPDATE TABLE Transacciones
-- id_transacciones INTEGER AUTOINCREMENT PRIMARY KEY

-- ALTER TABLE Propiedades ADD imagen TEXT NOT NULL;

-- INSERT INTO Registros(id_registro, email, contrasena) VALUES (1,"oscar.nic23@gmail.com", "123jshdf");

-- DELETE FROM Registros WHERE id_registro=1;

-- SELECT MAX(id_registro) FROM Registros;

-- CREATE PROCEDURE SP_ingresarUsuario (
-- @nombre varchar(10),
-- )
-- INSERT INTO Usuarios (nombre)
-- VALUES(@nombre)
-- GO

-- EXECUTE SP_ingresarUsuario "oscar"
