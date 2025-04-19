import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='moghithm@22', 
        database='prescription_db'
    )