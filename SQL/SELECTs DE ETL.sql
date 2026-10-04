--Dimension de jugadores

SELECT DISTINCT
	js.api_player_id AS id_jugador_oltp,
	js.nombre_jugador,
	js.nacionalidad AS nacionalidad_jugador,
	js.edad AS edad_jugador
FROM stage.JugadoresSeason2026 AS js

--Tabla de hechos

SELECT
	jg.id_jugador_skey,
	c.id_liga_skey,
	e.id_equipo_skey,
	js.goles,
	js.asistencias,
	(js.goles+js.asistencias) AS total_Goles_Asistencias
FROM stage.JugadoresSeason2026 AS js
JOIN 
	DW_JugadoresDeTemporada.dw.jugadores AS jg ON js.api_player_id = jg.id_jugador_oltp
JOIN
	DW_JugadoresDeTemporada.dw.competencia AS c ON js.liga = c.nombre_liga
JOIN 
	DW_JugadoresDeTemporada.dw.equipo AS e ON js.equipo = e.nombre_equipo