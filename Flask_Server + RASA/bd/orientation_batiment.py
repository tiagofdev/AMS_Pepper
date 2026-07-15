import os
import sqlite3


def init_data():
    db_path = 'bd/orientation_batiment.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    sql = '''
    CREATE TABLE IF NOT EXISTS orientations (
        place VARCHAR(255),
        description TEXT
    )'''

    cursor.execute(sql)

    cursor.execute('''INSERT INTO orientations (place, description) 
                  VALUES (?, ?)''',
                   ("salle 101", 'Salle située au premier étage du batîment du CERI, à gauche du hall.'))

    cursor.execute('''INSERT INTO orientations (place, description)
                  VALUES (?, ?)''',
                   ("salle 102", "Salle située au premier étage, à droite du hall."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("bâtiment administratif", "Le bâtiment administratif se trouve au rez-de-chaussée, en face de l'entrée principale."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("laboratoire de chimie", "Le laboratoire de chimie est situé dans le bâtiment des Sciences, au deuxième étage, au bout du couloir à droite."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("salle des professeurs", "La salle des professeurs se trouve dans le bâtiment principal, au premier étage, en face de la salle 101."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("amphi blaise", "L'amphithéâtre Blaise est situé dans le bâtiment du CERI, au rez-de-chaussée, à gauche en entrant."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("bâtiment iut", "Le bâtiment IUT se trouve à l'extrémité nord du campus, près du parking principal."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("bâtiment agrosciences", "Le bâtiment Agrosciences est situé à l'est du campus, à proximité de la bibliothèque universitaire."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("salle c137", "La salle C137 se trouve au bâtiment du CERI, au deuxième étage, au fond du couloir à gauche."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("cafétaria", "La cafétaria est située au batîment Agrosciences, à droite de l'entrée principale du campus."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("scolarité", "Le service de scolarité est situé dans le bâtiment administratif, au premier étage, au bureau 103."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("salle des robots", "Les salles de robots se trouvent dans le bâtiment des technologies, au rez-de-chaussée, à gauche du laboratoire d'informatique."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("toilettes", "Les toilettes se trouvent au rez-de-chaussée du batîment du CERI."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("bâtiment du ceri", "Le bâtiment du CERI est situé au sud du campus, à côté du batiment de l'Iut."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("salle 103", "La salle 103 est située dans le bâtiment administratif, au premier étage, à gauche de la salle des professeurs."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("amphi ada", "L'amphithéâtre Ada se trouve dans le bâtiment du CERI, au premier étage, juste après les escaliers principaux."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("laboratoire de physique", "Le laboratoire de physique est situé dans le bâtiment des sciences, au rez-de-chaussée, à droite du hall."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("bibliothèque universitaire", "La bibliothèque universitaire est située à côté de l'Agrosciences."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("bâtiment du crous", "Le bâtiment du CROUS est situé juste à côté de la cafétaria, au sud-est du campus, facilement accessible depuis l'entrée principale."))

    cursor.execute('''INSERT INTO orientations (place, description) 
                      VALUES (?, ?)''',
                   ("bureau du secrétariat", "Le bureau du secrétariat se trouve au rez-de-chaussée du bâtiment administratif, à droite après l'entrée principale."))

    print("Table schedule created successfuly ")

    conn.commit()
    conn.close()


def select_data_orientation(place):
    db_path = 'bd/orientation_batiment.db'

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    cursor.execute('''SELECT * FROM orientations WHERE place = ?''',(place,))

    rows = cursor.fetchall()

    if not rows:
        print("Aucune donnée trouvée pour les critères fournis.")
        conn.close()
        return None

    text = ""
    for row in rows:
        place, description = row
        text = f"Suivez cette description : {description}.\n"
        break

    conn.close()
    return text


if __name__ == '__main__':
    init_data()