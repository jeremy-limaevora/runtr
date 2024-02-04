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

        # Récupération des étudiants
        cursor = connection.cursor()
        query = "SELECT * FROM etudiant"
        cursor.execute(query)
        students = cursor.fetchall()

        # Affichage des résultats
        print("\nListe des étudiants :")
        for student in students:
            print(f"ID: {student[0]}, Nom: {student[1]}, Prénom: {student[2]}, Âge: {student[3]}, Email: {student[4]}")

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données : {err}")

finally:
    # Check if connection is not None before closing
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée")

