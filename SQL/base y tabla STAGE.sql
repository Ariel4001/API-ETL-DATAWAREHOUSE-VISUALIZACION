CREATE DATABASE Stage_Jugadores
GO

USE Stage_Jugadores
GO

CREATE SCHEMA stage
GO

CREATE TABLE stage.JugadoresSeason2026(
	api_player_id INT,
	nombre_jugador VARCHAR(100),
	edad INT,
	nacionalidad VARCHAR(100),
	equipo VARCHAR(100),
	liga VARCHAR(100),
	goles INT,
	asistencias INT
)
GO

SELECT
	*
FROM stage.JugadoresSeason2026
