from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)


@app.route('/')
def news_work():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    db_session.global_init('db/🅰️🅱️🅾️🅱️🅰️.sqlite')
    app.run(host='0.0.0.0', port=8080)