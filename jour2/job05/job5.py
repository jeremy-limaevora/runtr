import mysql.connector

# Informations de connexion à la base de données
host = "localhost"
database = "LaPlateforme"
user = "root"
password = "Laplateforme1"

# Initialize connection variable to None
connection = None

try:
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        print("Connecté à la base de données")

        # Exécution de la requête pour calculer la superficie totale des étages
        cursor = connection.cursor()
        query = "SELECT SUM(superficie) AS superficie_totale FROM etage"
        cursor.execute(query)
        total_superficie = cursor.fetchone()[0]

        # Affichage du résultat
        print(f"La superficie de La Plateforme est de {total_superficie} m2")

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données : {err}")

finally:
    # Check if connection is not None before closing
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée")
