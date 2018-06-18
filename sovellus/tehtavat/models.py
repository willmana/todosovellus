from sovellus import db
from sovellus.models import Base
from sqlalchemy.orm import relationship
from sovellus.kategorialuokat.models import Kategoria

association_table = db.Table('task_category', Base.metadata,
    db.Column('tehtava_id', db.Integer, db.ForeignKey('tehtava.id')),
    db.Column('kategoria_id', db.Integer, db.ForeignKey('kategoria.id'))
)

class Tehtava(Base):

    __tablename__ = 'tehtava'

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    categories = relationship("Kategoria", secondary=association_table)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, categories):
        self.name = name
        self.done = False
        self.categories = categories

    @staticmethod
    def tasks_by_account(id):
        return db.session().query(Tehtava).filter_by(account_id=id).all()

    @staticmethod
    def all_by_ids(ids):
        ret = []
        for t in db.session().query(Tehtava).filter(Tehtava.id.in_(ids)):
            print(t)
            ret.append(t)
        return ret
