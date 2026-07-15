import os
import sqlite3


def init_data():
    db_path = 'bd/schedule.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    sql = '''
    CREATE TABLE IF NOT EXISTS schedule (
        section VARCHAR(255),
        groupe VARCHAR(255),
        name_edt VARCHAR(255),
        salle VARCHAR(255),
        time_edt VARCHAR(255),
        date VARCHAR(255),
        site VARCHAR(255),
        enseignant VARCHAR(255),
        duree VARCHAR(255)
    )'''

    cursor.execute(sql)

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("m1 ia", "classique", "gestion de projet", "salle S2", "11h", "aujourd'hui", "ceri", "Monsieur Paul",
                    "2h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("master 1 intelligence artificielle", "classique", "gestion de projet", "salle S2", "11h", "aujourd'hui", "ceri",
                    "Monsieur Paul",
                    "2h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (
                   "m1 ilsen", "classique", "AMS-Project", "salle 128", "8h-30", "aujourd'hui", "ceri", "Monsieur LeFevre",
                   "3h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("m1 ilsen", "classique", "Anglais", "salle 127", "13h", "aujourd'hui", "ceri", "Prof anglais", "3h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("master 1 ingénierie logiciel", "classique", "Anglais", "salle 127", "13h", "aujourd'hui", "ceri", "Prof anglais",
                    "3h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("l1 histoire", "groupe 1", "Histoire", "salle 128", "14h", "20 décembre", "avignon centre",
                    "Monsieur Jean", "1h30min"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (
                   "m2 ilsen", "alternant", "Apprentissage automatique", "salle 137", "16h", "demain", "ceri", "Monsieur Yannick",
                   "3h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("m1 ilsen", "classique", "Techniques de test", "salle 102", "09h", "vendredi", "ceri",
                    "Monsieur Salas",
                    "2h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("master 1 ingénierie logiciel", "classique", "Techniques de test", "salle 102", "09h", "05 mai", "ceri",
                    "Monsieur Salas",
                    "2h"))

    cursor.execute('''INSERT INTO schedule(section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("master 1 ingénierie logiciel", "classique", "Techniques de test", "salle 102", "09h", "19 avril",
                    "ceri", "Monsieur Salas", "2h"))


    print("Table schedule created successfuly ")

    conn.commit()
    conn.close()


def select_data_schedule(section, groupe, date):
    db_path = 'bd/schedule.db'

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    cursor.execute('''SELECT * FROM schedule WHERE section = ? AND groupe = ? AND date = ?''',
                   (section, groupe, date))

    rows = cursor.fetchall()

    if not rows:
        print("Aucune donnée trouvée pour les critères fournis.")
        conn.close()
        return None

    seen = {}
    text = "Votre emploi du temps pour:\n"

    for row in rows:
        section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree = row
        key = (section, groupe, name_edt, salle, time_edt, date, site, enseignant, duree)
        if key not in seen:
            seen[key] = True
            text += f"- Le cours {name_edt} aura lieu dans la {salle} à {time_edt} avec l'enseignant {enseignant} pour une durée de {duree}.\n"

    conn.close()
    return text


if __name__ == '__main__':
    init_data()
