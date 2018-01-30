import MySQLdb
import csv
from datetime import datetime, date
import pandas as pd


#Connect to a MYSQL database
con = MySQLdb.connect(host= 'localhost', port =3306, db ='Suppliers', user = 'root', passwd = 'Password05')
c = con.cursor() #create a cursor that we can use to execute SQL statement

header = ['Supplier Name','Invoice Number','Par Number','Cost','Purchase Date']

c.execute("SELECT * FROM supplier WHERE Cost >300;")
rows = c.fetchall()
data = []
for row in rows:
    data.append(row)

data =pd.DataFrame(data, index=None, columns= header)
write_excel = pd.ExcelWriter('test.xlsx') #output the result to excel file
data.to_excel(write_excel, 'sheet1')
write_excel.save()