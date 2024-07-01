import psycopg

# Verbindungsinformationen zur Datenbank
dbname = 'test'
user = 'marvinrogg'
password = ''
host = 'localhost'  # Hier kann auch eine IP-Adresse stehen, wenn die Datenbank auf einem anderen Rechner liegt
port = '5432'  # Standard-Port für PostgreSQL

# Verbindung zur Datenbank herstellen
try:
    connection = psycopg.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Verbindung zur Datenbank hergestellt.")

    # Hier kannst du Datenbankoperationen ausführen

    # Beispiel: Datenbankabfrage
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM passwords;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Website: {row[1]}, Benutzername: {row[2]}, Passwort: {row[3]}")

    # Beispiel: Daten einfügen
    # cursor.execute("INSERT INTO deine_tabelle (spalte1, spalte2) VALUES (%s, %s)", (wert1, wert2))
    # connection.commit()

except psycopg.Error as e:
    print("Fehler beim Verbinden zur Datenbank:", e)

finally:
    # Verbindung schließen
    if connection:
        cursor.close()
        connection.close()
        print("Verbindung zur Datenbank geschlossen.")

        #test
        #test neuer Branch
        ## neuer Test
