import sqlite3

def crearConexion():
    conn = sqlite3.connect('database/database.db')
    return conn.cursor()