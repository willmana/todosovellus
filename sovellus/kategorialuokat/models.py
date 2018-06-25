from sovellus import db
from sovellus.models import Base
from sqlalchemy import text
class Kategoria(Base):

    __tablename__="kategoria"

    name = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def categories_by_user(id):
        return db.session().query(Kategoria.id, Kategoria.name).filter_by(account_id=id).all()

    @staticmethod
    def all_by_id(ids):
        ret = []
        for c in db.session().query(Kategoria).filter(Kategoria.id.in_(ids)):
            print(c)
            ret.append(c)
        return ret

    @staticmethod
    def listaa_tehtavat(id):
        stmt = text('SELECT tehtava.name FROM task_category, tehtava, kategoria'
        ' WHERE task_category.kategoria_id = ' + str(id) +
        ' AND task_category.kategoria_id = kategoria.id'
        ' AND task_category.tehtava_id = tehtava.id')

        res = db.engine.execute(stmt)
        tehtavat = []
        for row in res:
            tehtavat.append(row[0])
        return tehtavat
