import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
query = """CREATE TABLE STUDENT (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, 
AGE INT NOT NULL, ADDRESS CHAR(50), ROLLNO REAL)"""
conn.execute(query)
print("Table created successfully")


# Step-2: Inserting into a Table

query = """ INSERT INTO STUDENT(ID,NAME,AGE,ADDRESS,ROLLNO) VALUES (1, 'Paul', 32, 
 'California', 21040 ) """
conn.execute(query)
conn.commit() 
print("Records created successfully")


query = """ INSERT INTO STUDENT(ID,NAME,AGE,ADDRESS,ROLLNO) VALUES (1, 'Paul', 32, 
 'California', 21040 ) """
conn.execute(query)
conn.commit()
print("Records created successfully")
cursor = conn.execute("SELECT id, name, address, rollno from STUDENT")
for row in cursor:
 print("ID = 1 ", row[0])
print("NAME = Paul ", row[1])
print("ADDRESS = 32,'California' ", row[2])
print("ROLLNO = 21040" , row[3])
print("Operation done successfully")
conn.close()


cursor = conn.execute("DELETE FROM STUDENT WHERE ID = 1")
print("Record delete successfully")
conn.close()