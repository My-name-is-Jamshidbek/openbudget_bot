import sqlite3
from datetime import datetime

def baseadd(user_id,chat_id,tel_number):
        try:
            connection = sqlite3.connect("botbaza.db")
            crsr = connection.cursor()
            crsr.execute(f"""INSERT INTO royxatdanotganlar VALUES (
            '{tel_number}',
            '{user_id}',
            '{chat_id}'
            )""")
            connection.commit()
            connection.close()
            return True
        except:return False
def basebanadd(tel_number):
    try:
        connection = sqlite3.connect("botbaza.db")
        crsr = connection.cursor()
        crsr.execute(f"""INSERT INTO bloklanganlar VALUES (
        '{tel_number}'
        )""")
        connection.commit()
        connection.close()
        return True
    except:return False

def basebantek(tel_number):
    try:
        conn = sqlite3.connect("botbaza.db")
        c = conn.cursor()
        c.execute(f"""SELECT * FROM bloklanganlar WHERE telefonraqam = '{tel_number}'""")
        i = c.fetchall()
        if len(i) == 0:
            return True
        else:return False
    except:return False
def basetek(tel_number):
    try:
        conn = sqlite3.connect("botbaza.db")
        c = conn.cursor()
        c.execute(f"""SELECT * FROM royxatdanotganlar WHERE telefonraqam = '{tel_number}'""")
        i = c.fetchall()
        if len(i) == 0:
            return True
        else:return False
    except:return False