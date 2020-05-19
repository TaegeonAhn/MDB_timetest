import pyodbc
import csv
import time


start = time.time() #시작 시간 저장
# MS ACCESS DB CONNECTION
conn_str = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별7.mdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

for table_info in cursor.tables(tableType ='TABLE'):
    str_table = table_info.table_name
    print(str_table)


print("소요시간 : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

cursor.close()
conn.close()