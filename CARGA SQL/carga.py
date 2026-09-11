import pandas as pd
from sqlalchemy import create_engine
import os


def cargar_stage_a_sql():
    #Ruta del archivo CSV generado
    csv_path = "../EXTRACCION/stage_data/stage_goleadores_global.csv"

    if not os.path.exists(csv_path):
        print(f"No se encontró el archivo CSV en: {csv_path}. Revisar script de extraccion")
        return

    print("Leyendo archivo CSV local...")
    df = pd.read_csv(csv_path)
    print(f"Se leyeron {len(df)} registros del archivo.")

    #Configuración de la conexión a SQL Server
    servidor = r"LAPTOP-6K5K4L9B\CASTROARISQL"
    base_datos = "Stage_Jugadores"
    usuario = "sa"
    contraseña = "sa"

    # Cadena de conexión con credenciales
    conexion_str = f"mssql+pyodbc://{usuario}:{contraseña}@{servidor}/{base_datos}?driver=ODBC+Driver+17+for+SQL+Server"

    print("Conectando a SQL Server...")
    try:
        engine = create_engine(conexion_str)

        #Cargar el DataFrame a la tabla dentro del schema 'stage'
        df.to_sql(
            name='JugadoresSeason2026',
            con=engine,
            schema='stage',
            if_exists='append',
            index=False
        )

        print("¡Éxito! Los datos fueron volcados correctamente en la tabla `stage.JugadoresSeason2026`.")

    except Exception as e:
        print(f"Error al conectar o cargar los datos en SQL Server: {e}")


if __name__ == "__main__":
    cargar_stage_a_sql()