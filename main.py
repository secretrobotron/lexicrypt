from flask import (Flask, request, session, g, redirect,
                  url_for, abort, render_template, flash)

from lexicrypt import Lexicrypt
import settings

app = Flask(__name__)

if settings.DEBUG:
    app.debug = True


@app.route('/')
def main():
    lex = Lexicrypt()
    message = u'this is the message this is the message this is the message'
    lex.encrypt_message(message)
    dmessage = lex.decrypt_message('static/encrypted/test.png')
    return render_template('index.html', page='home',
                                         message=message,
                                         dmessage=dmessage)


if __name__ == '__main__':
    app.run()
