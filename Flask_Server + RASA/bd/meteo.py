import os
import sqlite3

def init_data():
    db_path = "bd/meteo.db"
    print(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully connected to SQLite3")

    sql = '''
    CREATE TABLE IF NOT EXISTS meteo (
        moment TEXT NOT NULL,
        temperature REAL NOT NULL,
        humidity REAL NOT NULL,
        wind_speed REAL NOT NULL,
        wind_direction REAL NOT NULL,
        precipitation REAL NOT NULL,
        weather_condition TEXT NOT NULL,
        pressure REAL NOT NULL,
        visibility REAL NOT NULL
   )
    '''

    cursor.execute(sql)

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("matin", 12.0, 70.0, 8.0, "Ouest", 0.0, "Brumeux", 1011.0, 9.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("soir", 16.0, 65.0, 10.0, "Sud", 0.0, "Clair", 1013.0, 12.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("minuit", 10.0, 80.0, 4.0, "Nord", 0.0, "Froid", 1010.0, 5.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("nuit", 12.0, 85.0, 5.0, "Nord-Ouest", 0.0, "Humide", 1010.0, 6.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("05h du matin", 8.0, 90.0, 3.0, "Nord", 0.0, "Gelée", 1008.0, 4.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("weekend", 18.0, 60.0, 10.0, "Sud", 0.0, "Clair", 1013.0, 15.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("matinée", 14.0, 72.0, 6.0, "Ouest", 0.0, "Brumeux", 1011.0, 8.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("fin d'après-midi", 22.0, 48.0, 13.0, "Sud-Ouest", 0.0, "Chaud", 1016.0, 18.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("pendant le déjeuner", 20.0, 45.0, 12.0, "Est", 0.0, "Ensoleillé", 1014.0, 14.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("tôt le matin", 9.0, 85.0, 5.0, "Nord-Ouest", 0.0, "Gelée", 1009.0, 6.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("19h", 8.0, 90.0, 3.0, "Nord", 0.0, "Gelée", 1008.0, 4.0))

    cursor.execute('''INSERT INTO meteo (moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   ("cet instant", 8.0, 90.0, 3.0, "Nord", 0.0, "Gelée", 1008.0, 4.0))

    print("Tables created and data inserted successfully........")

    conn.commit()
    conn.close()

def select_data_meteo(moment):
    db_path = 'bd/meteo.db'

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    cursor.execute('''SELECT * FROM meteo WHERE moment = ?''',(moment,))

    rows = cursor.fetchall()

    if not rows:
        print("Aucune donnée trouvée pour les critères fournis.")
        conn.close()
        return None

    text = ""
    for row in rows:
        moment, temperature, humidity, wind_speed, wind_direction, precipitation, weather_condition, pressure, visibility = row
        text = (f"l'information pour la météo : \n"
                f"temperature = {temperature}, \n"
                f"precipitation = {precipitation}, \n"
                f"weather_condition = {weather_condition}")

        break

    conn.close()
    return text


# Main function
if __name__ == "__main__":
    init_data()