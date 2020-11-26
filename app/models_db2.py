from sqlalchemy import ForeignKey
from app import db

class All_mixin(object):
    """ This mixin is included in all of the sqlalchemy models.
    """
    __bind_key__ = "db2" # SQLALCHEMY_BINDS in config.py

    def __str__(self):
        return str(self.id)


class Employee(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Numeric(precision=9, asdecimal=False))
    married = db.Column(db.Boolean(),nullable=False)

    company_id =  db.Column(
        db.Integer,
        ForeignKey("company.id", ondelete="SET NULL", onupdate="CASCADE")
    ) # employer
    company = db.relationship('Company', back_populates='employees')
    country_id = db.Column(
        db.Integer,
        ForeignKey("country.id", ondelete="SET NULL", onupdate="CASCADE")
    )
    country = db.relationship('Country', back_populates='employees')

    def __str__(self):
        return self.last_name


class Company(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    industries = db.Column(db.String(255), nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    fiscal_year = db.Column(db.Integer, nullable=False)
    num_employees = db.Column(db.Integer, nullable=False)
    market_cap = db.Column(db.Float, nullable=False)
    headquarters = db.Column(db.String(255), nullable=False)
    rev_per_employee = db.Column(db.Float, nullable=True)
    employees = db.relationship('Employee', back_populates='company')

    # The return value is displayed in tables that reference this class.
    def __str__(self):
        return self.name


class Country(db.Model, All_mixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    political_system = db.Column(db.String(255),nullable=False)
    population = db.Column(db.Float, nullable=False)
    employees = db.relationship('Employee', back_populates='country')

    def __str__(self):
        return self.name
