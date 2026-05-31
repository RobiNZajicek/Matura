import sqlite3

con = sqlite3.connect("user.db")

cur = con.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")

cur.execute("INSERT INTO users(name,age) VALUES(?,?)",("Robin",12))
cur.execute("INSERT INTO users(name,age) VALUES(?,?)",("Adan",29))
cur.execute("INSERT INTO users(name,age) VALUES(?,?)",("Kuba",39))
cur.execute("INSERT INTO users(name,age) VALUES(?,?)",("Krystof",19))
con.commit()

cur.execute("SELECT * FROM users")

users = cur.fetchall()

for i in users:
   print(i)
sort_age = sorted(users, key=lambda x: x[2])
print('sorted')
for item in sort_age:
   print(item)   

cur.execute("UPDATE users SET age=? WHERE name=?",(20,'Robin'))

con.close()


