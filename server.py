from flask import Flask, render_template, redirect, abort, request
from data import db_session
from data.jobs import Jobs
from data.users import User
from forms.user import RegisterForm
from forms.login_form import LoginForm
from forms.job_add import JobForm
from flask_login import login_user, LoginManager, logout_user, login_required, current_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.secret_key = 'assdasdasdasdasd'


@app.route('/')
def news_work():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/addjob', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            job=form.job_title.data,
            team_leader_id=form.team_leader.data,
            work_size=form.work_size.data,
            collaborations=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('job.html', title='Adding job', form=form)


@app.route('/editjob/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = JobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         ((Jobs.team_leader_id == current_user.id) | (current_user.id == 1))
                                         ).first()

        if job:
            form.job_title.data = job.job
            form.work_size.data = job.work_size
            form.team_leader.data = job.team_leader_id
            form.is_finished.data = (True if job.is_finished else False)
            form.collaborators.data = job.collaborations
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         ((Jobs.team_leader_id == current_user.id) | (current_user.id == 1))
                                         ).first()
        if job:
            job.job = form.job_title.data
            job.work_size = form.work_size.data
            job.team_leader_id = form.team_leader.data
            job.is_finished = form.is_finished.data
            job.collaborations = form.collaborators.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('job.html',
                           title='Edit job',
                           form=form
                           )


@app.route('/deletejob/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id,
                                     ((Jobs.team_leader_id == current_user.id) | (current_user.id == 1))
                                     ).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


if __name__ == '__main__':
    db_session.global_init('db/🅰️🅱️🅾️🅱️🅰️.sqlite')
    app.run(host='0.0.0.0', port=8080)
