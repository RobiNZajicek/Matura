import sqlite3
con = sqlite3.connect("users.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER) ")

cur.execute("INSERT INTO users(name,age) VALUES(?,?)",('Robin',19) )
cur.execute("INSERT INTO users(name,age) VALUES(?,?)",('Krystof',12) )
cur.execute("INSERT INTO users(name,age) VALUES(?,?)",('Adam',21) )
cur.execute("INSERT INTO users(name,age) VALUES(?,?)",('Kuba',30) )
cur.execute('SELECT * FROM users')

users = cur.fetchall()
for i in users:
    print(i) 


nejmladsi = sorted(users,key=lambda x: x[2])
print('nejmladsi ')
print('----------------------------------------------------------------------------------------------------')
for nej in nejmladsi:
    print(nej)
cur.execute(
    "DELETE FROM users WHERE name=?",
    ("Robin",)
)
user_objects = []
class User:
    def __init__(self,idi,name,age):
        self.idi = idi
        self.name = name 
        self.age = age
    def __str__(self):
        return f'uzivatel {self.name} s id :{self.idi} je stary {self.age} let '
    
for row in users:
    user = User(row,[0],row[1],row[2])
    user_objects.append(user)

for useros in user_objects:
    print(useros)
con.commit()
    
