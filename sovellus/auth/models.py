from sovellus import db
from sovellus.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"


    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Tehtava", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_no_tasks():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Tehtava ON Tehtava.account_id = Account.id"
                     " WHERE (Tehtava.done IS null OR Tehtava.done = 1)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Tehtava.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
