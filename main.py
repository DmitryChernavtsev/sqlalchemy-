# noinspection PyUnresolvedReferences
from data.jobs import Jobs
import datetime
from flask import Flask, render_template, redirect
# noinspection PyUnresolvedReferences
from data import __all_models
# noinspection PyUnresolvedReferences
from data import db_session
# noinspection PyUnresolvedReferences
from data.users import User



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    db_sess = db_session.create_session()
    user = db_sess.query(User).all()
    jobs = db_sess.query(Jobs).all()
    user_name = {i.id: [i.surname, i.name] for i in user}
    return render_template("index.html", jobs=jobs, names=user_name)

def main():
    db_session.global_init("db/mars_explorer.db")
    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user = User()
    # user.surname = "France"
    # user.name = "Chris"
    # user.age = 25
    # user.position = "soldier"
    # user.speciality = "engineer"
    # user.address = "module_7"
    # user.email = "chris_soldier@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user = User()
    # user.surname = "Mainer"
    # user.name = "Robert"
    # user.age = 22
    # user.position = "soldier"
    # user.speciality = "engineer"
    # user.address = "module_10"
    # user.email = "Robert_soldier@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    #
    # user = User()
    # user.surname = "Lannister"
    # user.name = "Joyfree"
    # user.age = 27
    # user.position = "efreitor"
    # user.speciality = "spesialist"
    # user.address = "module_14"
    # user.email = "Joyfree_spesialist@mars.org"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()