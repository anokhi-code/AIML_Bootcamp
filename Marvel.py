#create database connection
import os
from dotenv import load_dotenv
import mysql
import mysql.connector
load_dotenv() 

class MarvelConnector:
    database_connector = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "gladiator"),

    )

    cur = database_connector.cursor()
    cur.execute("DROP TABLE IF EXISTS marvel")
    cur.execute("""
CREATE TABLE IF NOT EXISTS marvel (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    height float,
    weight float,
    games_played INT
)
""")

    def clear_marvel(self):
        sql = "DELETE FROM marvel"
        self.cur.execute(sql)
        self.database_connector.commit()
        print("Marvel table cleared")
    

    def insert_marvel(self):
        sql = "INSERT INTO marvel "
        val = """VALUES (1, "IronMan", 180, 75, 120),
        (2, "SpiderMan", 170, 65, 110),
        (3, "Hulk", 200, 140, 90),  
        (4, "Thor", 195, 100, 130),
        (5, "Captain America", 188, 90, 105)
        """
        self.cur.execute(sql + val)
        self.database_connector.commit()

    def view_marvel(self):
        self.cur.execute("SELECT * FROM marvel")
        result = self.cur.fetchall()
        for row in result:
            print(row)

    def __del__(self):
        self.database_connector.close()
        print("Connection closed")

# MarvelConnector().insert_marvel()
if __name__ == "__main__":
    connector = MarvelConnector()
    connector.clear_marvel()
    connector.insert_marvel()
    connector.view_marvel()
    del connector  # This will call __del__()

