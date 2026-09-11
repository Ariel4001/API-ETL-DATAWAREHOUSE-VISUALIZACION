import requests
import pandas as pd
import os


def extraer_multiples_goleadores():
    url = "https://v3.football.api-sports.io/players/topscorers"
    headers = {
        # En la documentacion solo permite el token de la siguiente manera y a continuacion la clave API
        # de mi cuenta creada
        'x-apisports-key': 'b1b6925605afeeb49b3b6c4124b4d098'
    }

    # diccionario de ligas a consultar
    ligas_a_consultar = [
        {"id": 39, "nombre": "Premier League", "season": 2024},
        {"id": 140, "nombre": "La Liga", "season": 2024},
        {"id": 135, "nombre": "Serie A", "season": 2024},
        {"id": 78, "nombre": "Bundesliga", "season": 2024},
        {"id": 61, "nombre": "Ligue 1", "season": 2024}
    ]

    todos_los_goleadores = []

    print("Iniciando extracción masiva de múltiples ligas...")

    # Recorremos cada liga con un bucle
    for liga in ligas_a_consultar:
        params = {
            "league": liga["id"],
            "season": liga["season"]
        }

        print(f"Consultando {liga['nombre']}...")
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            # Procesamos los datos de esta liga en específico
            for item in data.get('response', []):
                player = item.get('player', {})
                stats = item.get('statistics', [{}])[0]
                team = stats.get('team', {})
                goals_info = stats.get('goals', {})

                # asignamos la variable para mapear cada columna y agregarla al diccionario
                jugador_dict = {
                    'api_player_id': player.get('id'),
                    'nombre_jugador': player.get('name'),
                    'edad': player.get('age'),
                    'nacionalidad': player.get('nationality'),
                    'equipo': team.get('name'),
                    'liga': liga['nombre'],
                    'goles': goals_info.get('total', 0),
                    'asistencias': goals_info.get('assists', 0)
                }
                todos_los_goleadores.append(jugador_dict)
        else:
            print(f"Error al consultar {liga['nombre']}: {response.status_code}")

    # creamos el dataframe del diccionario
    df = pd.DataFrame(todos_los_goleadores)
    return df


if __name__ == "__main__":
    df_resultado = extraer_multiples_goleadores()
    # creamos la carpeta y dentro de la carpeta el archivo stage
    if not df_resultado.empty:
        os.makedirs("stage_data", exist_ok=True)
        csv_path = "stage_data/stage_goleadores_global.csv"
        df_resultado.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"\n¡Capa Stage global generada con éxito en: {csv_path}!")
        print(f"Total de registros obtenidos: {len(df_resultado)}")
        print(df_resultado.head(10))
    else:
        print("No se pudieron obtener datos.")

