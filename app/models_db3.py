from sqlalchemy import ForeignKey, func
from app import db

class All_mixin(object):
    """ This mixin is included in all of the sqlalchemy models.
    """
    __bind_key__ = "db3" # SQLALCHEMY_BINDS in config.py

    def __str__(self):
        return str(self.id)


class User(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    pets = db.relationship('Pet', back_populates='owner')
    posts = db.relationship('Post', back_populates='user')

    def __str__(self):
        return self.name


class Post(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    user_id =  db.Column(
        db.Integer,
        ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    user = db.relationship('User', back_populates='posts')
    created_at = db.Column(db.DateTime, server_default=func.now())


class Pet(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    animal = db.Column(db.String(255), nullable=False)
    owner_id =  db.Column(
        db.Integer,
        ForeignKey("user.id", ondelete="SET NULL", onupdate="CASCADE")
    )
    owner = db.relationship('User', back_populates='pets')
    weight_lb = db.Column(db.Numeric(precision=5, asdecimal=False))
    weight_kg = db.Column(db.Numeric(precision=5, asdecimal=False))
    weight_st = db.Column(db.Numeric(precision=5, asdecimal=False))

    def __str__(self):
        return self.name
