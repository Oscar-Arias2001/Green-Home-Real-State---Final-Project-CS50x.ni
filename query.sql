-- CREATE TABLE "Registros"(
--     id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
--     email TEXT NOT NULL,
--     contrasena TEXT NOT NULL
-- );
-- DELETE FROM Registros WHERE id_registro = 1;
-- DELETE FROM Usuarios WHERE codigo_usuario = 1;
-- DROP TABLE Registros;
-- DROP TABLE Usuarios;

-- CREATE TABLE "Suscripcion"(
--     id_plan INTEGER PRIMARY KEY AUTOINCREMENT,
--     tipo_plan TEXT NOT NULL,
--     precio REAL NOT NULL
-- );
-- UPDATE Suscripcion SET tipo_plan = "Anual" WHERE id_plan = 1;
-- UPDATE Suscripcion SET tipo_plan = "Mensual" WHERE id_plan = 2;

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

-- CREATE TABLE "Usuarios_Suscripcion" (
--     id_usuario_suscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
--     id_registro INTEGER NOT NULL,
--     id_suscripcion INTEGER NOT NULL,
--     FOREIGN KEY(id_registro) REFERENCES Registros(id_registro),
--     FOREIGN KEY(id_suscripcion) REFERENCES Suscripcion(id_plan)
-- );

-- CREATE TABLE "Transacciones"(
--     id_transacciones INTEGER PRIMARY KEY,
--     codigo_tipo_transaccion INTEGER,
--     codigo_propiedad INTEGER,
--     codigo_interesado INTEGER,
--     FOREIGN KEY(codigo_tipo_transaccion) REFERENCES Tipo_Transaccion(codigo_transaccion)
--     FOREIGN KEY(codigo_propiedad) REFERENCES Propiedades(codigo_propiedad)
--     FOREIGN KEY(codigo_interesado) REFERENCES Usuarios(codigo_usuario)
-- );
-- DROP TABLE Propiedades;
-- CREATE TABLE "Tipo_Transaccion"(
--     codigo_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
--     descripcion TEXT NOT NULL
-- );

-- CREATE TABLE "Tipo_Inmueble"(
--     codigo_tipo INTEGER PRIMARY KEY AUTOINCREMENT,
--     descripcion TEXT NOT NULL
-- );

-- CREATE TABLE "Ciudad"(
--     codigo_ciudad INTEGER PRIMARY KEY AUTOINCREMENT,
--     nombre TEXT NOT NULL
-- );

-- CREATE TABLE "Propiedades"(
--     codigo_propiedad INTEGER PRIMARY KEY AUTOINCREMENT,
--     direccion TEXT NOT NULL,   
--     precio REAL NOT NULL,
--     moneda TEXT NOT NULL,
--     codigo_ciudad INTEGER,
--     tipo_inmueble INTEGER,
--     codigo_usuario_suscripcion INTEGER NOT NULL,
--     tipo_transaccion INTEGER NOT NULL,
--     estado TEXT NOT NULL,
--     FOREIGN KEY(codigo_ciudad) REFERENCES Ciudad(codigo_ciudad),
--     FOREIGN KEY(tipo_inmueble) REFERENCES Tipo_Inmueble(codigo_tipo),
--     FOREIGN KEY(codigo_usuario_suscripcion) REFERENCES Usuarios_Suscripcion(id_usuario_suscripcion),
--     FOREIGN KEY(tipo_transaccion) REFERENCES Tipo_Transaccion(codigo_transaccion)
-- );

ALTER TABLE Propiedades ADD COLUMN imagen TEXT NOT NULL; 
ALTER TABLE Propiedades ADD COLUMN descripcion TEXT NOT NULL; 
