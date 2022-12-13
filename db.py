import sqlite3

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
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text, \
        high_score_pokemon int, high_score_superhero int,\
        times_played_pokemon int, times_played_superhero int)")
    db_close()

def change_pokemon_high_score(username, new_high_score):
    c = db_connect()
    c.execute('UPDATE users SET high_score_pokemon=? WHERE username=?',\
            (new_high_score,username))
    db_close()

def change_superhero_high_score(username, new_high_score):
    c = db_connect()
    c.execute('UPDATE users SET high_score_superhero=? WHERE username=?',\
            (new_high_score,username))
    db_close()

# increments times_played_pokemon by 1
def increment_times_played_pokemon(username):
    c = db_connect()
    c.execute('SELECT times_played_pokemon from users WHERE username=?',(username,))
    data = c.fetchone()
    # print(data)
    c.execute('UPDATE users SET times_played_pokemon=? WHERE username=?',\
            (data[0]+1,username))
    db_close()

def increment_times_played_superhero(username):
    c = db_connect()
    c.execute('SELECT times_played_superhero from users WHERE username=?',(username,))
    data = c.fetchone()
    # print(data)
    c.execute('UPDATE users SET times_played_superhero=? WHERE username=?',\
            (data[0]+1,username))
    db_close()

def get_rankings_pokemon():
    '''returns a sorted list of tuples (username, high_score)'''
    c = db_connect()
    c.execute('SELECT username,high_score_pokemon from users')
    data = c.fetchall()
    db_close()
    # print(data)
    data.sort(key=lambda row: row[1], reverse=True)
    # print(data)
    return data

def get_rankings_superhero():
    '''returns a sorted list of tuples (username, high_score)'''
    c = db_connect()
    c.execute('SELECT username,high_score_superhero from users')
    data = c.fetchall()
    db_close()
    # print(data)
    data.sort(key=lambda row: row[1], reverse=True)
    # print(data)
    return data

def get_top_players(num):
    '''returns top {num} players from get_rankings'''
    return get_rankings()[:num]

# for signing up
def check_user_not_exists(username):
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?',(username,))
    username_status = c.fetchone()
    db_close()
    # print(username_status)
    # print(username)
    return username_status == None

def get_pokemon_average(username):
    '''returns score/times_played'''
    c = db_connect()
    c.execute('SELECT high_score_pokemon,times_played_pokemon FROM users WHERE username=?',(username,))
    data = c.fetchone()
    print(data)
    db_close()
    if data[1] != 0:
        return data[0] / data[1]
    return None

# for signing up
def create_new_user(username, password):
    c = db_connect()
    c.execute('INSERT INTO users VALUES (?,?,0,0,0,0)',(username, password))
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

if __name__ == '__main__':
    db_table_inits()
    increment_times_played_superhero('a')
    change_pokemon_high_score('b',21)
    increment_times_played_pokemon('b')
    increment_times_played_pokemon('b')
    change_superhero_high_score('c',10)
    get_pokemon_average('b')
    # print(get_top_players(3))
    print(get_pokemon_average('b'))
    # # get_rankings()
