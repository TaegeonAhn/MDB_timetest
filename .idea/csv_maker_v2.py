import pyodbc
import csv

# MS ACCESS DB CONNECTION
pyodbc.lowercase = False
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별7.mdb;')
cursor = conn.cursor()

cursor.execute("SELECT * FROM 환자정보");

# OPEN CSV AND ITERATE THROUGH RESULTS

with open('D:\타사B migration test\새파일2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in cursor.fetchall() :
        writer.writerow(row)

cursor.close()
conn.close()