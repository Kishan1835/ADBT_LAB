import mysql.connector
# // check ur password
mydb = mysql.connector.connect(host="localhost", user="root", password="Tsk@2003")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS vysya")
mydb.database = 'vysya'
mycursor.execute("CREATE TABLE IF NOT EXISTS mca (Name VARCHAR(255), College VARCHAR(255))")
sql = "INSERT INTO mca (Name, College) VALUES (%s, %s)"
val = ("Uday", "salem")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record inserted.") 
mycursor.execute("SELECT * FROM mca") 
myresult = mycursor.fetchall()
for x in myresult: 
    print(x)

mycursor.close()
mydb.close()

