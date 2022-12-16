import sqlite3
from datetime import datetime

class DBOps():
    conn = None
    cursor = None
    
    def __init__(self):
        if DBOps.conn is None:
            try:
                DBOps.conn = sqlite3.connect('data.db', check_same_thread=False)
                DBOps.cursor = DBOps.conn.cursor()
            except Exception as error:
                print("Error: Connection could not be established {}".format(error))
            else:
                print("Connection established!")
        
        self.conn = DBOps.conn
        self.cursor = DBOps.cursor
    
    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS recipetable(title TEXT, ingredients TEXT, procedure TEXT, postdate DATE)')
        
    def add_recipe(self, title, ingredients, procedure):
        self.cursor.execute('INSERT INTO recipetable(title, ingredients, procedure, postdate) VALUES (?,?,?,?)', (title, ingredients, procedure, datetime.now().date()))
        self.conn.commit()
        
    def view_all_recipes(self):
        self.cursor.execute('SELECT DISTINCT title from recipetable')
        data = self.cursor.fetchall()
        return data
    
    def get_recipe(self, title):
        self.cursor.execute('SELECT * FROM recipetable WHERE title=(?)', (title,))
        data = self.cursor.fetchall()
        return data
    
    def remove_recipe(self, title):
        self.cursor.execute('DELETE FROM recipetable WHERE title=(?)', (title,))
        self.conn.commit()