import MySQLdb
import csv
from datetime import datetime, date


#Connect to a MYSQL database
con = MySQLdb.connect(host= 'localhost', port =3306, db ='Suppliers', user = 'root', passwd = 'Password05')
c = con.cursor() #create a cursor that we can use to execute SQL statement

#Insert / add records in the table "supplier"
filewriter = csv.writer(open('supplier_list.csv', 'w',newline=''), delimiter = ",")
header = ['Supplier Name','Invoice Number','Par Number','Cost','Purchase Date']
filewriter.writerow(header)

c.execute("SELECT * FROM supplier WHERE Cost >300;")
rows = c.fetchall()

for row in rows:
    filewriter.writerow(row)

