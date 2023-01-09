import sqlite3

samle_data = sqlite3.connect("data.db")
cursor_obj = samle_data.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS DATA")

table = """create table (
            Email varchar(255) NOT NULL,
            First_Name char(25) NOT NULL,
            Last_Name char(25),
            score INT
        ):"""

cursor_obj.execute(table)
print("you are good to go")
samle_data.close()