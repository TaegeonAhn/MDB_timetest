import pyodbc
import csv
import time

# MS ACCESS DB CONNECTION
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별7.mdb;')
cursor = conn.cursor()

start = time.time() #시작 시간 저장
str_table = '환자정보'
cursor.execute('SELECT * FROM {}'.format(str_table));

# OPEN CSV AND ITERATE THROUGH RESULTS
columns = [column[0] for column in cursor.description] # 컬럼명 출력

with open('D:\타사B migration test\새파일6.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns)

    for row in cursor.fetchall() :
        writer.writerow(row)

print("time : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

cursor.close()
conn.close()