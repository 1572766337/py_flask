#coding=utf8

#flask轻博客

# all the imports

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
	 render_template, flash
app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config['DATABASE'] = 'test.db'
app.config['USERNAME'] = 'root'
app.config['PASSWORD'] = '123'

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv
	
def init_db():
	# with app.app_context():
	with connect_db() as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

init_db()
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid username or password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

@app.route('/')
def show_entries():
	with connect_db() as db:
		cur = db.execute('select title, text from entries order by id desc')
		entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html', entries=entries)
	
@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	with connect_db() as db:
		db.execute('insert into entries (title, text) values (?, ?)',
						 [request.form['title'], request.form['text']])
		db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))
	
if __name__ == '__main__':
	app.run()