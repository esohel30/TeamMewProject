import sqlite3, random as rand

DB_FILE = "data.db"

db = None

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

# creates a table if it doesn't exist
def db_table_inits():
    c = db_connect()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text, high_score int)")
    db_close()

# def delete_tables():
#     c = db_connect()
#     for :
#         c.execute("DROP TABLE ?",(,))
#     db_close()


# for signing up
def check_user_not_exists(username):
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?',(username,))
    username_status = c.fetchone()
    db_close()
    # print(username_status)
    # print(username)
    return username_status == None
    # if user:
    #     return False
    # return True

# for signing up
def create_new_user(username, password):
    c = db_connect()
    c.execute('INSERT INTO users VALUES (?,?,0)',(username, password))
    db_close()


# for logging in
# checks if there exists username and password in db, returns True if there is
def check_credentials(username, password):
    c = db_connect()
    c.execute('SELECT username,password FROM users WHERE username=? AND password=?',(username, password))
    # for row in c:
    #     print(row)
    user_status = c.fetchone()
    # print(user)
    db_close()
    return user_status != None
    # if user:
    #     return True
    # return False
