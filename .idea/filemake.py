import pyodbc
import time
import sys
import csv

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별7.mdb;')
cursor = conn.cursor()

start = time.time() #시작 시간 저장

def output_col(col):
    if col:
        if isinstance(col,unicode):
            return col.encode('utf-8')
        else:
            return str(col)
    else:
        return ''

cursor.execute('select * from 환자정보')
row = cursor.fetchone()

fname = sys.argv[2]

with open(fname,'w',encoding='utf-8',newline='' ) as f:
    writer =csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONE)

    writer.writerow([t[0] for t in row.cursor_description])
    while 1:
        if not row:
            break
        writer.writerow(map(output_col, row))
        row = cursor.fetchone()

#for row in cursor.fetchall():
 #   f.write(row)
  #  print (row)
#    repr(row)
#    f.write(row)

#f.close()
#print("time : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간


conn.close()