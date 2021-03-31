from data import db_session
from data.jobs import Jobs
from data.users import User

db_session.global_init('🅰️🅱️🅾️🅱️🅰️.sqlite')
session = db_session.create_session()

list_persons = [('Адам', 'Бущкар', 14), ('Костя', 'Тодыщев', 88),
                ('Дачеслав', 'Жмулов', 19)]

list_jobs = [(1, 'Создание новичкама', 228, '1, 2', False),
             (2, 'razrabotka kolca nuitona', 2, '1', False),
             (3, 'Телепорт из Нахабино', 1488, '0, 1', False)]

for x in list_persons:
    user = User(name=x[0], surname=x[1], age=x[2])
    session.add(user)

for x in list_jobs:
    job = Jobs(team_leader_id=x[0], job=x[1], work_size=x[2], collaborations=x[3],
               is_finished=x[4])
    session.add(job)

session.commit()
