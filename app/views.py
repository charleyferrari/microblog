from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}
	posts = [  # fake array of posts
		        { 
		            'author': {'nickname': 'John'}, 
		            'body': 'Beautiful day in Portland!' 
		        },
		        { 
		            'author': {'nickname': 'Susan'}, 
		            'body': 'The Avengers movie was so cool!' 
		        }
    		]
	return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	name = None
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('login.html', title='Sign In', form=form, name=name)