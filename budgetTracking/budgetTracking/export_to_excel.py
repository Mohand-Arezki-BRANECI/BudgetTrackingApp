import pandas as pd
import mysql.connector
import os
import platform
from datetime import datetime

def get_download_path():
    if platform.system() == "Windows":
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    elif platform.system() == "Darwin":
        return os.path.join(os.environ["HOME"], "Downloads")
    else:
        return os.path.join(os.environ["HOME"], "Downloads")

def export_to_excel():
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

        # Générer le nom de fichier avec la date et l'heure actuelles
        excel_title = datetime.now().strftime('%Y%m%d_Export_tableau_gestion_%H%M')
        print(excel_title)
        file_name = f'{excel_title}.xlsx'
        print(file_name)

        # Chemin du fichier de sortie
        download_path = get_download_path()
        output_file = os.path.join(download_path, file_name)
        
        # Exporter les données en Excel avec la feuille nommée "activite"
        df.to_excel(output_file, index=False, sheet_name='activite')

        # Exporter les données en Excel
        df.to_excel(output_file, index=False)

        print(f"Les données ont été exportées avec succès dans '{output_file}'.")

        # Ouvrir le fichier Excel automatiquement
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
    export_to_excel()