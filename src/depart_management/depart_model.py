from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EmailType
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
import enum
from sqlalchemy import Enum


class Department(db.Model):
    __tablename__ = "department"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # department (parent) table is primary key for employee table - one to many
    employees = db.relationship("Employee", uselist=False, back_populates="Department")

    departName = db.Column(
        db.Unicode(80),
        nullable=False
    )

    # noOfEmployee = db.Column(
    #     db.Unicode(80),
    #     nullable=False
    # )
