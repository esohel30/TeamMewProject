from flask import Flask,render_template,session,request,redirect
import secrets
from db import *

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

if __name__ == '__main__':
    app.debug = True
    app.run()
