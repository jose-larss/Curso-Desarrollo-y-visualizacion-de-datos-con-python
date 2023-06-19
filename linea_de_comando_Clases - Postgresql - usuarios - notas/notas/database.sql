CREATE DATABASE IF NOT EXISTS APPlineaComandoClases
USE APPlineaComandoClases

CREATE TABLE IF NOT EXISTS usuarios(
    id SERIAL PRIMARY KEY NOT NULL,
    nombre  varchar(150),
    apellido  varchar(150),
    email  varchar(50) NOT NULL UNIQUE,
    pass  varchar(50) NOT NULL,
    fecha date NOT null);

CREATE TABLE IF NOT EXISTS notas(
    id SERIAL PRIMARY KEY NOT NULL,
    usuarios_id integer REFERENCES usuarios(id) NOT NULL,
    titulo varchar(150) NOT NULL,
    contenido text,
    fecha date NOT NULL);