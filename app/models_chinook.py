from sqlalchemy import ForeignKey
from sqlalchemy.inspection import inspect
from app import db


class All_mixin(object):
    """ This mixin is included in all of the sqlalchemy models.
    """
    # __bind_key__ = None for default sqlalchemy database URI.
    __bind_key__ = None

    def __str__(self):
        """ The return value is displayed in tables that reference this class.
        Override this in child class to return another column (ie name).

        Returns
        -------
        primary key value : str(int)
        """
        pk = inspect(self).identity
        return str(pk)


class Album(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)

    artistid =  db.Column(
        db.Integer,
        ForeignKey("artist.id", ondelete="SET NULL", onupdate="SET NULL")
    )
    artist = db.relationship('Artist', back_populates='albums')


class Artist(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    albums = db.relationship('Album', back_populates='artist')

    def __str__(self):
        return self.name
