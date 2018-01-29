import MySQLdb
import csv
from datetime import datetime, date


#Connect to a MYSQL database
con = MySQLdb.connect(host= 'localhost', port =3306, db ='Suppliers', user = 'root', passwd = 'Password05')
c = con.cursor() #create a cursor that we can use to execute SQL statement


#Insert / add records in the table "supplier"
input_file = csv.reader(open('supplier.csv', 'r'), delimiter = ",")
header = next(input_file)
for rows in input_file:
    data = []
    for row_index in range(len(rows)):
        if row_index < 4:
            data.append(rows[row_index])
        else:
            a_date = datetime.date(datetime.strptime(str(rows[row_index]), '%d-%m-%y'))
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    c.execute("INSERT INTO supplier VALUES(%s,%s,%s,%s,%s)", data)
con.commit()


#Query the ssupplier table all
c.execute("SELECT * FROM supplier")
rows_list = c.fetchall()


#count the number of rows in the output
row_counter = 0
for row in rows_list:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(row[column_index])
    print(row_list_output)
    row_counter += 1
print("Number of rows : %d" % (row_counter))