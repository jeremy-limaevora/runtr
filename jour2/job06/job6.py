import mysql.connector


host = "localhost"
database = "LaPlateforme"
user = "root"
password = "Laplateforme1"


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

        # Exécution de la requête pour calculer la capacité totale des salles
        cursor = connection.cursor()
        query = "SELECT SUM(capacite) AS capacite_totale FROM salle"
        cursor.execute(query)
        total_capacite = cursor.fetchone()[0]

        # Affichage du résultat
        print(f"La capacité de toutes les salles est de : {total_capacite}")

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données : {err}")

finally:
    # Check if connection is not None before closing
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée")
