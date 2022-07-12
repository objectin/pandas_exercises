import sqlite3

# DB 생성 (오토 커밋)
conn = sqlite3.connect('test.db', isolation_level=None)
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS table1 \
    (id integer PRIMARY KEY, name text, birthday text)')

