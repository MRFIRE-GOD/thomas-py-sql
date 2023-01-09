import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password1222333",
  database="thomas-sql"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (First_Name, Last_Name, E-post, address) VALUES (%s, %s)"
val = [
  ("Mira" , "Keller" ",biv-ikacore81@outlook.com","3816128043" ,"3530"), 
("Johan","Duke","kosidu-dori30@hotmail.com","4762614010","3530"),
("London","Cunningham","fadal_acize96@gmail.com","5576433285","3530"),
("Claire","Melton","leciy-ejuka9@aol.com","9153542265","3530"),
("Kareem","Garrison","mes_ozogasu99@outlook.com","6997949084","3530"),
("Kyler","Ferrell","leh-osucuko31@mail.com","2266909939","3530"),
("Camryn","Carver","sayeru_vuru32@aol.com","3135307725","3530"),
("Edith","Campbell,xikide_bebo26@yahoo.com","9924509590","3530"),
("Reed","Glover","vigowe-jepe60@hotmail.com","3854671000","3530"),
("Cailyn,Hobbs","vadot-apuwe65@mail.com","7109785329","3530"),
("Jade","Mosley","bose_wituwu7@aol.com","8297933744","3530"),
("Deandre","Daugherty","suru-wonocu12@outlook.com","3174116246","3530"),
("Dallas","Pruitt","ram_efexopa73@yahoo.com","5624299561","3530"),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")