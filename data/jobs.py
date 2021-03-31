from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer, primary_key=True,
                   autoincrement=True)
    team_leader_id = sa.Column(sa.Integer,
                            sa.ForeignKey('users.id'))
    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    collaborations = sa.Column(sa.String)
    start_date = sa.Column(sa.DateTime)
    end_date = sa.Column(sa.DateTime)
    is_finished = sa.Column(sa.Boolean)
    team_leader = orm.relation('User')