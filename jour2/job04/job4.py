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

        # Récupération des noms et capacités de la table "salle"
        cursor = connection.cursor()
        query = "SELECT nom, capacite FROM salle"
        cursor.execute(query)
        rooms = cursor.fetchall()

        # Affichage des résultats
        print("\nNoms et capacités des salles :")
        for room in rooms:
            print(f"Nom: {room[0]}, Capacité: {room[1]}")

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données : {err}")

finally:
    # Check if connection is not None before closing
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée")
