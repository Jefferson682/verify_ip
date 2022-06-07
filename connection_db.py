import sqlite3

# Database connection
def consult(sql):
    try:
        sqliteConnection = sqlite3.connect('address_ip.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
    except sqlite3.Error as error:
        return {"error" : error}
    finally:
        return lista


def alterData(sql):
    try:
        sqliteConnection = sqlite3.connect('address_ip.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(sql)
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
    except sqlite3.Error as error:
        return {"error" : error}
    finally:
        return True
    

    

