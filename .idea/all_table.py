import pyodbc
import csv
import time

start = time.time() #시작 시간 저장
# MS ACCESS DB CONNECTION
conn_str = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별9.mdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

table_name_list = []

for table_info in cursor.tables(tableType ='TABLE'):
    table_name_list.append(table_info.table_name)

print(table_name_list)

for table_name in table_name_list:
    print(table_name)

    with open('D:\타사B migration test\{}.csv'.format(table_name), 'w', newline='') as f:
        writer=csv.writer(f)
        cursor.execute ('SELECT * FROM {}'. format(table_name))
        columns = [column[0] for column in cursor.description] # 컬럼명 출력
        writer.writerow(columns)
        for row in cursor.fetchall():

            writer.writerow(row)


print("소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

cursor.close()
conn.close()