# -*- coding: utf-8 -*-

from flask import Flask, url_for, request, render_template, make_response
app = Flask(__name__)



@app.route('/')
def index():
    username = request.cookies.get('username')
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username','flask')
    return resp


@app.route('/hello')
def hello_flask():
    return '3-2 Hello Flask!!'

@app.route('/hello/')
def hello():
    return '/hello/flask!!'

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : ' + username

@app.route('/profile_method', methods=['POST','GET'])
def profile(username=None):
    error = None
    if request.method =='POST':
        username = request.form['username']
        email = request.form['email']

    if request.method == 'GET':
        username = request.args.get('username')
        email = request.args.get('email')
        print(username)
        print(email)




    error = 'Invalid username or email'

    return render_template('profile.html', error=error,username=username, email=email)
    #url 호출 시 username 과 email 을 get, post  방식별로 어떻게 던져주지??


@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d' %message_id




if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('hello'))
        print(url_for('get_profile', username='flask'))

    app.run()
