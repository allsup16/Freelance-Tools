import sys
import os
import sqlite3
path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','SQL'))
sys.path.insert(0,path)
import sql

#use for non select statements
def general_statement(database_name,table_name):
    conn = sqlite3.connect(f'{database_name}.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    query = 'enter statement using statement builder in sql.py'
    cursor.execute(query)
    conn.commit()
    conn.close()

#use for select statements
def fetch_one_statement(database_name,table_name):
    conn = sqlite3.connect(f'{database_name}.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    query = 'enter statement using statement builder in sql.py'
    cursor.execute(query)
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result

#use for select statements
def fetch_all_statement(database_name,table_name):
    conn = sqlite3.connect(f'{database_name}.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    query = 'enter statement using statement builder in sql.py'
    cursor.execute(query)
    result=cursor.fetchall()
    conn.commit()
    conn.close()
    return result