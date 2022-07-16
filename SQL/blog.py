import sqlite3
from pprint import pprint

conn = sqlite3.connect('blog.db')
c = conn.cursor()

# c.execute('''CREATE TABLE blog (id integer PRIMARY KEY, subject text, content text, date text)''')
# c.execute("INSERT INTO blog VALUES (1, '첫 번째 블로그', '첫 번째 블로그입니다.', '20190827')")
# c.execute("INSERT INTO blog VALUES (2, '두 번째 블로그', '두 번째 블로그입니다.', '20190827')")
_id = 3
subject = "세 번째 블로그"
content = "세 번째 블로그입니다."
date = "20190827"
# c.execute("INSERT INTO blog VALUES (%d, '%s', '%s', %s)" % (_id, subject, content, date))
_id = 4
subject = '네 번째 블로그'
content = '네 번째 블로그입니다.'
date = '20190827'

blog5 = {
    "id": 5,
    "subject": "다섯 번째 블로그",
    "content": '다섯 번쨰 블로그입니다.',
    'date': '20190827',
}
# c.execute("INSERT INTO blog VALUES (:id, :subject, :content, :date)", blog5)

# print(c.execute("SELECT * FROM blog").fetchone())

# c.execute('INSERT INTO blog VALUES (?, ?, ?, ?)', (_id, subject, content, date))
c.execute("UPDATE blog SET subject='최초의 블로그' WHERE id=1")

c.execute("DELETE FROM blog WHERE id=5")

all = c.execute('Select * From blog')
pprint(all.fetchall())

conn.commit()
conn.close()
