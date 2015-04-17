from flask import render_template, flash, redirect
from app import application
from .forms import LoginForm

@application.route('/')
@application.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user = user, title = 'Home', posts = posts)

@application.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)
