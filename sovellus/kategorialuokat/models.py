from sovellus import db
from sovellus.models import Base

class Kategoria(Base):

    __tablename__="kategoria"

    name = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
