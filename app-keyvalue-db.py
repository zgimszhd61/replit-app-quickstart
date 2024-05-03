from replit import db

## 存储数据，读取数据.
# db['a'] = 'aaaaaa'

## 根据key来查询.
# print(db['a'])

## 查询有哪些keys
keys = db.keys()
for item in keys:
  print(item)
