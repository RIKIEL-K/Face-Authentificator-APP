import sqlite3

DB_NAME = "users_faces.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Création de la table `users`
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        password TEXT ,
        face_descriptor BLOB
    )
    ''')

    conn.commit()
    conn.close()
    print("Base de données créée avec succès !")

# Fonction pour ajouter un utilisateur
def add_user(name, email, password, face_descriptor=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO users (name, email, password,face_descriptor)
        VALUES (?, ?, ?, ?)
        ''', (name, email, password, face_descriptor))

        conn.commit()
        print("Utilisateur ajouté avec succès !")
    except sqlite3.IntegrityError:
        print("cet email est déjà enregistré.")
    finally:
        conn.close()

# Fonction pour récupérer les informations d'un utilisateur
def login_user(email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        print(f"Connexion réussie ! Bienvenue {user[1]}")
        return True
    else:
        print("Email ou mot de passe incorrect.")
        return False

# Exécution du script principal
if __name__ == "__main__":
    create_database()