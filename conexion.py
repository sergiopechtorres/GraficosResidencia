from sqlalchemy import create_engine
import mysql.connector
import pandas as pd 

db= "anuarios"
table = "data"
path= "Data.xlsx"

url= "mysql+mysqlconnector://root:""@localhost/"

engine= create_engine(url + db , echo = False)

df= pd.read_excel(path)

print("Read ok")

df.to_sql (name= table, con=engine, if_exists='append', index=False)

ver = pd.read_sql_query("SELECT * FROM Data", engine)
print(ver)
