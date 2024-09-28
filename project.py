# importing modules 
import mysql.connector
import pandas as pd

print("modules imported ")
# making a connection 

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='car_sales'
)
cursor = conn.cursor()

print("connection got created ")

cursor.execute("select * from sales_customer;")
data= cursor.fetchall()
df=pd.DataFrame(data)
print(data)