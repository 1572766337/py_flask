#coding=utf8

#redirect

from flask import abort, redirect, url_for,Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
	
if __name__ == '__main__':
	app.run()