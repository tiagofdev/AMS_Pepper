import os
import sqlite3

def init_data():
    db_path = 'bd/texter_prof.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully connected to SQLite3")

    sql = '''
    CREATE TABLE IF NOT EXISTS enseignants (
        nom_prof_tp VARCHAR(255),
        formation_occupee_tp VARCHAR(255),
        niveau_tp VARCHAR(255),
        email VARCHAR(255)
    );
    '''

    cursor.execute(sql)

    cursor.execute('''INSERT INTO enseignants (nom_prof_tp, formation_occupee_tp, niveau_tp, email)
                           VALUES (?, ?, ?, ?)''',
                   ("paul", "physique", "l1 sciences", "jeanpaul99@gmail.com"))

    cursor.execute('''INSERT INTO enseignants (nom_prof_tp, formation_occupee_tp, niveau_tp, email)
                           VALUES (?, ?, ?, ?)''',
                   ("diallo", "math", "l1 math", "momo@gmail.com"))

    cursor.execute('''INSERT INTO enseignants (nom_prof_tp, formation_occupee_tp, niveau_tp, email)
                           VALUES (?, ?, ?, ?)''',
                   ("lefevre", "ams-projet", "m1 informatique", "lefevre@univ.fr"))

    cursor.execute('''INSERT INTO enseignants (nom_prof_tp, formation_occupee_tp, niveau_tp, email)
                           VALUES (?, ?, ?, ?)''',
                   ("bernard", "chimie", "l2 chimie", "bernard.c@gmail.com"))

    cursor.execute('''INSERT INTO enseignants (nom_prof_tp, formation_occupee_tp, niveau_tp, email)
                           VALUES (?, ?, ?, ?)''',
                   ("sophie", "devops", "master 1 ilsen", "devops.de@univ.fr"))

    print("Table created enseignants successfully")

    conn.commit()
    conn.close()

def select_data_send_message(nom_prof_tp):
    db_path = 'bd/texter_prof.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    cursor.execute('''SELECT * FROM enseignants WHERE nom_prof_tp = ?''',
                   (nom_prof_tp, ))

    rows = cursor.fetchall()

    if not rows:
        print("Aucune donnée trouvée pour les critères fournis.")
        conn.close()
        return None

    text = ""
    for row in rows:
        nom_prof_tp, formation_occupee_tp, niveau_tp, email = row
        text = f"{email}.\n"
        break

    conn.close()
    return text

if __name__ == '__main__':
    init_data()