import pyodbc
import time

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별7.mdb;')
cursor = conn.cursor()

start = time.time() #시작 시간 저장

cursor.execute('select  * from 환자정보')
columns = [column[0] for column in cursor.description] # 컬럼명 출력


for row in cursor.fetchall():
    print(columns)
    print (row)


print("time : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

conn.close()