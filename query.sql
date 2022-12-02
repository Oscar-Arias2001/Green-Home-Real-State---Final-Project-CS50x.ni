-- CREATE TABLE "Registros"(
--     id_registro INTEGER PRIMARY KEY,
--     email TEXT NOT NULL,
--     contrasena TEXT NOT NULL
-- );

-- CREATE TABLE "Suscripcion"(
--     id_plan INTEGER PRIMARY KEY,
--     tipo_plan TEXT NOT NULL,
--     precio REAL NOT NULL
-- );

-- CREATE TABLE "Pais"(
--     id_pais INTEGER PRIMARY KEY,
--     nombre_pais TEXT NOT NULL
-- );

-- CREATE TABLE "Tipo_Transaccion"(
--     codigo_transaccion INTEGER PRIMARY KEY,
--     descripcion TEXT NOT NULL
-- );

-- CREATE TABLE "Tipo_Inmueble"(
--     código_tipo INTEGER PRIMARY KEY,
--     descripcion TEXT NOT NULL
-- );

-- CREATE TABLE "Ciudad"(
--     código_ciudad INTEGER PRIMARY KEY,
--     nombre TEXT NOT NULL,
--     codigo_pais INTEGER NOT NULL,
--     FOREIGN KEY(codigo_pais) REFERENCES Pais(id_pais)
-- );

-- CREATE TABLE "Usuarios_Suscripcion"(
--     id_usuario_suscripcion INTEGER PRIMARY KEY,
--     id_registro INTEGER NOT NULL,
--     id_suscripcion INTEGER NOT NULL,
--     FOREIGN KEY(id_registro) REFERENCES Registros(id_registro)
--     FOREIGN KEY(id_suscripcion) REFERENCES Suscripcion(id_plan)
-- );

-- CREATE TABLE "Usuarios"(
--     codigo_usuario INTEGER PRIMARY KEY,
--     nombre_completo TEXT NOT NULL,
--     telefono INTEGER NOT NULL,
--     id_registro INTEGER,
--     domicilio TEXT NOT NULL,
--     ciudad TEXT NOT NULL,
--     codigo_pais INTEGER,
--     FOREIGN KEY(id_registro) REFERENCES Registros(id_registro)
--     FOREIGN KEY(codigo_pais) REFERENCES Pais(id_pais)
-- );

-- CREATE TABLE "Propiedades"(
--     codigo_propiedad INTEGER PRIMARY KEY,
--     direccion TEXT NOT NULL,
--     ciudad TEXT NOT NULL,
--     precio REAL NOT NULL,
--     moneda TEXT NOT NULL,
--     tipo_inmueble INTEGER,
--     codigo_usuario_suscripcion INTEGER,
--     estado TEXT NOT NULL,
--     FOREIGN KEY(tipo_inmueble) REFERENCES Tipo_Inmueble(codigo_tipo)
--     FOREIGN KEY(codigo_usuario_suscripcion) REFERENCES Usuarios_Suscripcion(id_usuario_suscripcion)
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

ALTER TABLE Propiedades ADD imagen TEXT NOT NULL;


