from data import db_session
from data.jobs import Jobs
from data.users import User
from datetime import datetime

db_session.global_init('db/🅰️🅱️🅾️🅱️🅰️.sqlite')
session = db_session.create_session()

list_persons = [('Бушакур', 'Адам', 14, 'Квншик', 'Главный шутник', 'Украина', 'adamlubit@inetolko.ru'),
                ('Тодыщев', 'Костя', 88, 'DogHunter', 'Уничтожитель собак', 'start up 18', 'todishev@hunter.ru'),
                ('Дачеслав', 'Жмулов', 19, 'Командир комнаты грязи', 'уборка', 'NaHaBiNo', 'Jmuda2004@below.ru'),
                ('Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org')]

list_jobs = [(4, 'deployment of residential modules 1 and 2', 15, '2, 3', False),
             (1, 'Создание новичкама', 228, '1, 2', False),
             (3, 'Телепорт из Нахабино', 1488, '0, 1', False)]

for x in list_persons:
    user = User(surname=x[0], name=x[1], age=x[2], position=x[3], speciality=x[4], address=x[5], email=x[6])
    session.add(user)

for x in list_jobs:
    job = Jobs(team_leader_id=x[0], job=x[1], work_size=x[2], collaborations=x[3], start_date=datetime.now(),
               is_finished=x[4])
    session.add(job)

session.commit()
