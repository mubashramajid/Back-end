from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EmailType
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
import enum
from sqlalchemy import Enum


class Department(db.Model):
    __tablename__ = "Department"
    __table_args__ = {

    }
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    firstName = db.Column(
        db.Unicode(80),
        nullable=False
    )
    lastName = db.Column(
        db.Unicode(80),
        nullable=False
    )
    departName = db.Column(
        db.Unicode(80),
        nullable=False
    )
    employeeDesignation = db.Column(
        db.Unicode(80),
        nullable=False
    )
    teamName = db.Column(
        db.Unicode(80),
        nullable=False
    )
