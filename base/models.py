from base import db

class Message(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    date = db.Column(db.String(), nullable=False, unique=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Message {self.name}'