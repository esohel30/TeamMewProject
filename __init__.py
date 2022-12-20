from flask import Flask,render_template,session,request,redirect
import secrets
from db import *
from random import randint
from api import *
from game import *

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

# @app.route('/gameLanding')
# def gameLanding():
#     return render_template('gameLanding.html')

@app.route('/leaderboard')
def display_leaderboard():
    if 'username' not in session:
        return redirect('/login')
    pokemon_rankings = get_rankings_pokemon()
    superhero_rankings = get_rankings_superhero()
    return render_template('leaderboard.html',pokemon_rankings=pokemon_rankings, superhero_rankings=superhero_rankings)

@app.route('/pokemongame',methods=['GET','POST'])
def pokemongame():
    if 'username' not in session:
        return redirect('/login') 
    if request.method == 'POST':
        if 'guess' in request.form:
            is_correct = pokemon_check_answer(request.form['guess'], session['answer'])
            gif = get_yes_no_gif(is_correct)
            return render_template('/gif.html',gif=gif,score=get_score(),question_num=get_question_num()-1)
        if get_question_num() > 10:
            return redirect('/results')
    else:
        reset()
    info = generatepokemonquestion()
    img = info[0]
    question = info[1]
    answer = info[2]
    session['answer'] = answer
    if question == "Who's that pokemon?": 
        return render_template('/pokemongame1.html', img = img, question = question)
    return render_template('/pokemongame2.html', img = img, question = question)

@app.route('/superhero-game',methods=['GET','POST'])
def superhero_game():
    if 'username' not in session:
        return redirect('/login') 
        # return render_template('login.html',access_denied=True)
    if request.method == 'POST':
        print(request.form)
        if 'character' in request.form:
            is_correct = check_answer(request.form['character'])
            gif = get_yes_no_gif(is_correct)
            return render_template('/gif.html',gif=gif,score=get_score(),question_num=get_question_num()-1)
        # print(f'score: {SCORE}')
        # print(f'question #: {QUESTION_NUM}')
        if get_question_num() > 10:
            return redirect('/results') 
    # else:
    #     reset()
    data = play_superhero_game()
    name1, img1 = data[0]
    name2, img2 = data[1]
    return render_template('/superhero-question.html',stat_type=get_stat_type(),\
    score=get_score(),question_num=get_question_num(),\
    char1=name1,char2=name2,img1=img1,img2=img2)

@app.route('/results')
def results():
    if 'username' not in session:
        return redirect('/login')
    # Make sure that the user just finished a game
    if playing_game():
        user = session['username']
        update_database_superhero(user,get_score())
        template = render_template('/results.html',score=get_score(),high_score=get_high_score_superhero(user),\
        times_played=get_times_played_superhero(user),average=get_superhero_average(user))
        reset()
    else:
        return redirect('/leaderboard')
    return template


# @app.route('/yesno')
# def display_gif():
#     yes_gif = get_yes_no_gif(True)
#     no_gif = get_yes_no_gif(False)
#     return render_template('/gif.html', yes_gif=yes_gif, no_gif=no_gif)

if __name__ == '__main__':
    app.debug = True
    app.run()
