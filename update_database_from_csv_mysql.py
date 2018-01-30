import MySQLdb
import csv
from datetime import datetime, date


#Connect to a MYSQL database
con = MySQLdb.connect(host= 'localhost', port =3306, db ='Suppliers', user = 'root', passwd = 'Password05')
c = con.cursor() #create a cursor that we can use to execute SQL statement


#Insert / add records in the table "supplier"
input_file = csv.reader(open('update_supplier.csv', 'r'), delimiter = ",")
header = next(input_file)
for rows in input_file:
    data = []
    for row_index in range(len(rows)):
        data.append(rows[row_index])

    c.execute("UPDATE supplier SET Cost = %s WHERE Supplier_Name = %s;", data)
con.commit()


#Query the ssupplier table all
# c.execute("SELECT * FROM supplier")
# rows_list = c.fetchall()


