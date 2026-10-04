USE [Stage_Jugadores]
GO

SELECT * FROM stage.JugadoresSeason2026
GO

CREATE DATABASE DW_JugadoresDeTemporada
GO

CREATE SCHEMA dw
GO

CREATE TABLE dw.jugadores(
	id_jugador_skey INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	id_jugador_oltp INT NOT NULL,
	nombre_jugador VARCHAR(100) NOT NULL,
	nacionalidad_jugador VARCHAR(100) NOT NULL,
	edad_jugador INT NOT NULL,
)
GO

CREATE TABLE dw.competencia(
	id_liga_skey INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	nombre_liga VARCHAR(100) NOT NULL
)
GO

CREATE TABLE dw.equipo(
	id_equipo_skey INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	nombre_equipo VARCHAR(100) NOT NULL
)
GO

CREATE TABLE dw.hechos_asistencias(
	id_hecho_skey INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	id_jugador_skey INT NOT NULL,
	id_liga_skey INT NOT NULL,
	id_equipo_skey INT NOT NULL,
	goles INT NOT NULL,
	asistencias INT NOT NULL,
	total_Goles_Asistencias INT NOT NULL,
	CONSTRAINT fk_jugador FOREIGN KEY(id_jugador_skey)
		REFERENCES dw.jugadores(id_jugador_skey),
	CONSTRAINT fk_liga FOREIGN KEY(id_liga_skey)
		REFERENCES dw.competencia(id_liga_skey),
	CONSTRAINT fk_equipo FOREIGN KEY(id_equipo_skey)
		REFERENCES dw.equipo(id_equipo_skey),
	CONSTRAINT ch_goles CHECK(goles >= 0),
	CONSTRAINT ch_asistencias CHECK(asistencias >= 0),
	CONSTRAINT ch_totalgya CHECK(total_Goles_Asistencias >= 0)
)
GO

USE DW_JugadoresdeTemporada
GO

--inserto primero los registros de las ligas y equipos disponibles ya que no poseen id propio por estar en una sola tabla stage 
--proveniente de la API
INSERT INTO DW_JugadoresDeTemporada.dw.competencia(nombre_liga)
SELECT DISTINCT
	liga
FROM stage.jugadoresseason2026
GO

INSERT INTO DW_JugadoresDeTemporada.dw.equipo(nombre_equipo)
SELECT DISTINCT
	equipo
FROM stage.jugadoresseason2026
GO
--dimension jugador y tabla de hechos se los ejecuta en SSIS, posteriormente se visualiza en power BI


SELECT 
	*
FROM dw.hechos_asistencias