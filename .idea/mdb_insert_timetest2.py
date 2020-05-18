import pyodbc
import time
from tqdm.notebook import tqdm

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\타사B migration test\챠트자료\월별6.mdb;')
cursor = conn.cursor()

start = time.time() #시작 시간 저장
i = 0

query = """
INSERT INTO 환자정보 (환자정보,주소,주민등록번호,전화번호,우편번호,주소2,메모1,메모2,증번호,피보험자,휴대폰번호,성별,나이)
VALUES({},{},{},{},{},{},{},{},{},{},{},{},{}).format(i,i,i,i,i,i,i,i,i,i,i,i,i)
"""

queries = []

for i in range(0,15000):
    i = i + 1


    for j in tqdm(queries):
        cursor.execute(query)
        conn.commit()

queries.append(query)

print("time : ", time.time() - start ) #현재시간 - 시작시간 = 실행 시간

conn.close()