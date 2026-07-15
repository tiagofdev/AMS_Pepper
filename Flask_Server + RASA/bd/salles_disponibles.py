import os
import sqlite3

db_path = 'bd/salles_disponibles.db'
def init_data():

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    sql = '''
    CREATE TABLE IF NOT EXISTS salles_disponibles (
        nom_salle VARCHAR(255),
        heure_salle VARCHAR(255),
        duree VARCHAR(255)
    );
    '''

    cursor.execute(sql)

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                  VALUES (?, ?, ?)''',
                   ("C128", "13h30", "deux heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("C137", "13h30", "une heure"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("S2", "16h30", "deux heures trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                          VALUES (?, ?, ?)''',
                   ("S3", "16h30", "quatre heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                              VALUES (?, ?, ?)''',
                   ("S3", "maintenant", "quatre heures trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("A101", "midi", "trois heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("B205", "13h30", "une heure trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("C301", "quatorze heures", "deux heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("D102", "16h30", "deux heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("E209", "midi", "quatre heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("F401", "10h", "trois heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                          VALUES (?, ?, ?)''',
                   ("F401", "dans 1h", "trois heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("G302", "11h", "deux heures trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("H104", "14h30", "une heure"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("I207", "13h30", "deux heures trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("J501", "08h", "quatre heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("K203", "09h", "une heure trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("L402", "15h", "trois heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("M105", "16h30", "deux heures trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("O503", "midi", "deux heures trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("P305", "17h", "deux heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("Q106", "11h", "trois heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("R211", "16h", "quatre heures"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("S504", "08h30", "une heure trente minutes"))

    cursor.execute('''INSERT INTO salles_disponibles (nom_salle, heure_salle, duree) 
                      VALUES (?, ?, ?)''',
                   ("T308", "09h", "deux heures"))

    print("Table salles_disponibles created successfuly ")

    conn.commit()
    conn.close()


def select_data_salles(heure_salle):
    # db_path = 'bd/salles_disponibles.db'
    # if not os.path.exists(db_path):
    #     print("Base de données introuvable, création en cours...")
    #     init_data()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Base de données 'schedule' connectée avec succès à SQLite")

    cursor.execute('''SELECT nom_salle, duree FROM salles_disponibles WHERE heure_salle = ?''', (heure_salle,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "Aucune salle trouvée à cette heure."

    unique_rows = list(set(rows))
    print("Contenu de unique_rows :", unique_rows)

    if len(unique_rows) == 1:
        nom_salle, duree = unique_rows[0]
        return f"La salle {nom_salle} est disponible à {heure_salle} pour une durée de {duree}."

    text = f"Les salles disponibles à l'heure {heure_salle} sont:\n"
    for nom_salle, duree in unique_rows:
        text += f"- Salle {nom_salle} pour une durée de {duree}\n"

    return text



if __name__ == '__main__':
    init_data()