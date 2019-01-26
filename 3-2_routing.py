# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_flask():
    return '3-2 Hello Flask!!'

if __name__ == '__main__':
    app.run()
