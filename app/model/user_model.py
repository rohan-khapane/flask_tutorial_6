from app.app import db

class User(db.Model):
    __tablename__='user'

    uid=db.Column(db.Integer,primary_key=True)
    name=db.Colum(db.String,nullable=False)
    age=db.Column(db.Integer)

    def __repr__(self):
        return f'Name {self.name} and age{self.age} and id {self.uid}'


