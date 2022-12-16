from flask import Flask,render_template,session,request,redirect
import secrets
from db import *
from random import randint
from api import *

app = Flask(__name__)

app.secret_key = secrets.token_bytes(32)

@app.route('/', methods=['GET','POST'])
def home():
    # if logged in
    if 'username' in session:
        user = session['username']
        return render_template('home.html',username=user)
    return render_template('landing.html')

@app.route('/login', methods=['GET','POST'])
def login():
    # try to login user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(request.form)
        db_table_inits()
        correct_credentials = check_credentials(username, password)
        if correct_credentials:
            session['username'] = username
            return redirect('/')
        else:
            return render_template('login.html', error = True)
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    # trying signing up
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db_table_inits()
        no_user_exists = check_user_not_exists(username)
        if no_user_exists:
            create_new_user(username, password)
            return redirect('/login')
        else:
            return render_template('signup.html', error=True)
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return render_template('landing.html')

@app.route('/gameLanding')
def gameLanding():
    return render_template('gameLanding.html')

@app.route('/leaderboard')
def display_leaderboard():
    pokemon_rankings = get_rankings_pokemon()
    superhero_rankings = get_rankings_superhero()
    return render_template('leaderboard.html',pokemon_rankings=pokemon_rankings, superhero_rankings=superhero_rankings)

@app.route('/pokemongame')
def pokemongame():
    if request.method = 'POST':
        if
    info = generatepokemonquestion()
    img = info[0]
    question = info[1]
    answer = info[2]
    if questions == "Who's that pokemon?":
        return render_template('/pokemongame1.html', img = img, question = question, answer = answer)
    if len(answer) == 2:
        type1 = answer[0]
        type2 = answer[1]
        return render_template('/pokemongame2.html', img = img, question = question, type1 = type1, type2 = type2)
    type1 = answer[0]
    return render_template('/pokemongame2.html', img = img, question = question, type1 = type1)

@app.route('/superhero-game')
def superhero_game():
    data = generatecharacterquestion()
    return render_template('/superhero-question.html',image1=data[1][1],image2=data[2][1])


@app.route('/yesno')
def display_gif():
    yes_gif = get_yes_no_gif(True)
    no_gif = get_yes_no_gif(False)
    return render_template('/gif.html', yes_gif=yes_gif, no_gif=no_gif)

if __name__ == '__main__':
    app.debug = True
    app.run()
