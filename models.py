from connection import db 
from sqlalchemy.sql import func

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), index = True, nullable=False)
    lastname = db.Column(db.String(100), index = True, nullable=False)
    email = db.Column(db.String(80), index = True, unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
    

    """Data models."""
# from . import db
