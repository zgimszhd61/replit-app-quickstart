import psycopg2

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(
    dbname="",
    user="", 
    password="",
    host= ""
)

# 创建一个 cursor 对象并执行 SQL 语句
cur = conn.cursor()
cur.execute("INSERT INTO mtable (content) VALUES ('example contenthahhaha');")
conn.commit()  # 提交事务

cur.execute("SELECT * FROM mtable;")
rows = cur.fetchall()
for row in rows:
  print(row)

# 关闭数据库连接
cur.close()
conn.close()
