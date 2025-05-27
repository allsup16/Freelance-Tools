import sqlite3

#Create/Delete tables
def create_table(database_name, table_name, primary_columns):
    conn = sqlite3.connect(f'{database_name}.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    if primary_columns:
        column_defs = [f"{col} {dtype}" for col, dtype in primary_columns.items()]
        key_names = ', '.join(primary_columns.keys())
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {', '.join(column_defs)},
            PRIMARY KEY ({key_names})
        );
        """
        cursor.execute(query)
    else:
        print('No valid keys')
        conn.close()
        return
    conn.commit()
    conn.close()
    return primary_columns
def drop_table(database_name,table_name):
    conn = sqlite3.connect(f'{database_name}.db') 
    cursor = conn.cursor()
    cursor.execute(f"""DROP TABLE {table_name}""")
    conn.commit()
    conn.close()
#Alter Table
def add_column(database_name,table_name,column):
    conn = sqlite3.connect(f'{database_name}.db') 
    cursor = conn.cursor()
    column_name = list(column.keys())[0]
    column_dataType = column[column_name] 
    if column:
        query = f"""
        ALTER TABLE  {table_name} 
        ADD COLUMN {column_name} {column_dataType} ;"""
        cursor.execute(query)
    else:
        print('Not valid columns')
        conn.close()
        return
    conn.commit()
    conn.close()
def delete_column(database_name, table_name,primary_columns,delete_column):
    temp = 'temp'
def update_row(database_name, table_name, updates: dict, where_clause: str, params: tuple):
    conn = sqlite3.connect(f'{database_name}.db')
    cursor = conn.cursor()
    set_clause = ', '.join([f"{column} = ?" for column in updates.keys()])
    query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
    cursor.execute(query, tuple(updates.values()) + params)
    conn.commit()
    conn.close()

#Retrieve all info
def show_columns(database_name,table_name):
    conn = sqlite3.connect(f'{database_name}.db')
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns_names=cursor.fetchall()
    conn.close()
    return columns_names
def all_info(database_name,table_name):
    conn = sqlite3.connect(f'{database_name}.db')
    cursor = conn.cursor()
    info = cursor.execute(f"SELECT * FROM {table_name}")
    info = info.fetchall()
    conn.close()
    return info

#Retrieve specific info
def retrieve_column_info(database_name,table_name,select):
    conn = sqlite3.connect(f'{database_name}.db')
    cursor = conn.cursor()
    chosen_categories = ', '.join(select)
    info = cursor.execute(f"SELECT {chosen_categories} FROM {table_name}")
    info = info.fetchall()
    conn.close()
    return info
def retrieve_column_instance(database_name,table_name,select,where):
    conn = sqlite3.connect(f'{database_name}.db')
    cursor = conn.cursor()
    chosen_categories = ', '.join(select)
    instance = cursor.execute(f"""
                            SELECT {chosen_categories} 
                            FROM {table_name}
                            WHERE {where}
 """)
    instance = instance.fetchone()
    conn.commit()
    conn.close() 
    return instance

#add/remove row info
def insert_into(database_name, table_name, values):
    conn = sqlite3.connect(f'{database_name}.db')
    cursor = conn.cursor()
    placeholders = ', '.join(['?'] * len(values))
    query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(query, values)
    conn.commit()
    conn.close()
def remove_info(database_name, table_name, where_clause, params):
    conn = sqlite3.connect(f'{database_name}.db')
    cursor = conn.cursor()
    query = f"DELETE FROM {table_name} WHERE {where_clause}"
    cursor.execute(query, params)
    conn.commit()
    conn.close()





