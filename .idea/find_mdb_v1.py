import pyodbc
import csv
import time

start = time.time() #시작 시간 저장
# MS ACCESS DB CONNECTION
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별7.mdb;')
cursor = conn.cursor()

systable = "SELECT * FROM MSysObjects"

cursor.execute(systable);

# OPEN CSV AND ITERATE THROUGH RESULTS

#table.to_csv (table_name + '.csv', index_label='index')

with open('D:\타사B migration test\새파일5.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in cursor.fetchall() :
        writer.writerow(row)

print("소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

cursor.close()
conn.close()