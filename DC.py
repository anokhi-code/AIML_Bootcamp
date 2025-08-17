#create database connection
import os
from dotenv import load_dotenv
import mysql
import mysql.connector
load_dotenv() 

class DCConnector:
    con = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "gladiator"),
    )
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS dc")
    cur.execute("""
CREATE TABLE IF NOT EXISTS dc (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    height float,
    weight float,
    games_played INT
)
""")
    
    def clear_dc(self):
        sql = "DELETE FROM dc"
        self.cur.execute(sql)
        self.con.commit()
        print("DC table cleared")
    

    def insert_dc(self):
        sql = "INSERT INTO dc "
        val = """VALUES (1, "BatMan", 180, 85, 105),
        (2, "SuperMan", 189, 95, 205),
        (3, "Harvedent", 181, 75, 55),  
        (4, "Henery", 176, 87, 25),
        (5, "Heralt", 184, 100, 45)
        """
        self.cur.execute(sql + val)
        self.con.commit()

    def view_dc(self):
        self.cur.execute("SELECT * FROM dc")
        result = self.cur.fetchall()
        for row in result:
            print(row)

    def __del__(self):
        self.con.close()
        print("Connection closed")

# MarvelConnector().insert_marvel()
if __name__ == "__main__":
    connector = DCConnector()
    connector.clear_dc()
    connector.insert_dc()
    connector.view_dc()
    del connector  # This will call __del__()
