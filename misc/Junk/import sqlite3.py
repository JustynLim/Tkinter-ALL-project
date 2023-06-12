import sqlite3
import hashlib
import uuid

user_table_definition = """
CREATE TABLE users (
    username TEXT,
    salt TEXT,
    hpassword TEXT
)"""
add_user_sql = "INSERT INTO users VALUES ('{}','{}','{}')"

connection = sqlite3.connect("./stackoverflowdb.db")
cursor = connection.cursor()

cursor.execute(user_table_definition)


# Add incoming user
username = "Bacon"
password = "This is a little better, but this is just an outline..."

salt = uuid.uuid4().hex
hashedpassword = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()

cursor.execute(add_user_sql.format(username, salt, hashedpassword))

# Check incoming user

username = "Bacon"
password = "This is a little better, but this is just an outline..."

row = cursor.execute("SELECT salt, hpassword FROM users WHERE username = '{}'".format(username)).fetchone()

salt, hpassword = row  # Unpacking the row information - btw this would fail if the username didn't exist

hashedIncomingPwd = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()

if hashedIncomingPwd == hpassword:
    print("Winner winner chicken dinner we have a live one!")
else:
    print("No access for you")



import sqlite3
import datetime



con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))

con.close()