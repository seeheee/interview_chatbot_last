import sqlite3
from .models import Question

def saveDBtable(db, data):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    sql = Question('가장', 'data')
    cur.executemany(sql, data)

    conn.commit()  # 트랜젝션의 내용을 DB에 반영함
    conn.close()

if __name__ == '__main__':
    f = open('가장.txt', 'r')

    tempFile = f.read().splitlines()
    f.close()

    # DB에 테이블 입력
    saveDBtable('testDB.db', tempFile)


