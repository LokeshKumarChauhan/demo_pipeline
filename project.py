# importing modules 
import mysql.connector
import pandas as pd

print("modules imported ")
# making a connection 
import credentials
d= credentials.data
conn = mysql.connector.connect(**d)
cursor = conn.cursor()

print("connection got created ")

cursor.execute("select * from sales_customer;")
data= cursor.fetchall()
df=pd.DataFrame(data)
print(data)