from data import db_session
from data.news import News
from data.users import User

db_session.global_init('sempai.sqlite')
session = db_session.create_session()

u_1 = User()
u_1.name = "Тобишев"
u_1.about = "Десять дней без аниме"
u_1.email = "to@bish.ru"
session.add(u_1)

u_2 = User()
u_2.name = "Slave"
u_2.about = "White Slave"
u_2.email = "slave@white.ru"
session.add(u_2)

session.commit()

user = session.query(User).first()
print(user.name)

a_user = session.query(User).filter(User.id > 1,
                                    User.email.notlike("%a%"))
