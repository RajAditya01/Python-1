import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
query = """CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, 
AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL)"""
conn.execute(query)
print("Table created successfully")
# Step-2: Inserting into a Table
query = """ INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS) VALUES (1, 'Aditya', 18, 'Ambala') """
conn.execute(query)
conn.commit()
print("Records created successfully")
# Step-3: Selection/Retrieve data from a Database
cursor = conn.execute("SELECT id, name, address, from COMPANY")
for row in cursor:
    print("ID = 1 ", row[0])
print("NAME = Aditya ", row[1])
print("ADDRESS = 18,'Ambala' ", row[2])
print("Operation done successfully")
#conn.close()
# Step-4: Deletion from Table:
cursor = conn.execute("DELETE FROM COMPANY WHERE ID = 1")
print("Record delete successfully")
conn.close()