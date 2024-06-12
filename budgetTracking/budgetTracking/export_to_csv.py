import pandas as pd
import mysql.connector
import os
import platform

def get_download_path():
    if platform.system() == "Windows":
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    elif platform.system() == "Darwin":
        return os.path.join(os.environ["HOME"], "Downloads")
    else:
        return os.path.join(os.environ["HOME"], "Downloads")

def export_to_csv():
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="budget_tracking"
        )

        # Requête SQL
        sql_query = "SELECT * FROM activite"

        # Lire les données dans un DataFrame
        df = pd.read_sql(sql_query, conn)

        # Chemin du fichier de sortie
        download_path = get_download_path()
        output_file = os.path.join(download_path, 'output.csv')

        # Exporter les données en CSV
        df.to_csv(output_file, index=False)

        print(f"Les données ont été exportées avec succès dans '{output_file}'.")

        # Ouvrir le fichier CSV automatiquement pour windows, macOS et Linux
        if platform.system() == "Windows":
            os.startfile(output_file)
        elif platform.system() == "Darwin":
            os.system(f"open '{output_file}'")
        else:
            os.system(f"xdg-open '{output_file}'")

    except Exception as e:
        print(f"Erreur: {e}")

    finally:
        # Fermer la connexion à la base de données
        if conn:
            conn.close()

if __name__ == "__main__":
    export_to_csv()
