#coding=utf8

#cookie

from flask import request,Flask,make_response,render_template
app = Flask(__name__)

@app.route('/')
def index():
	username = request.cookies.get('username')
	if username:
		return u"欢迎您：" + username
	else:
		resp = make_response(render_template("index6.html"))
		resp.set_cookie('username', 'cookie user')
		return resp
		
if __name__ == '__main__':
	app.run()