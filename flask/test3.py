#coding=utf8

#http请求方式

from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return '处理登陆'
    else:
        return '<form action="" method="post"><input type="submit" value="登陆"></form>'
		
if __name__ == '__main__':
    app.run()