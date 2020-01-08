from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from src import db
from flask_restplus import Resource
from src.app import api

class Team(db.Model):
    __tablename__ = "Team"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    teamName = db.Column(
        db.Unicode(80),
        nullable=False
    )

    teamMembers = db.Column(
        db.Integer,
        nullable=False
    )


class Department(db.Model):
    __tablename__ = "Department"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    departName = db.Column(
        db.Unicode(80),
        nullable=False
    )

    noOfEmployee = db.Column(
        db.Unicode(80),
        nullable=False
    )
    # Relationship with Employee Table - one to many
    department_FK = relationship("Department", uselist=False, back_populates="Employee")


class Reviews(db.Model):
    __tablename__ = "Reviews"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    initiateDate = db.Column(
        db.Date,
        nullable=False
    )

    completionDate = db.Column(
        db.Date,
        nullable=False
    )

    status = db.Column(
        db.Boolean,
        nullable=False
    )


class KPI(db.Model):
    __tablename__ = "KPI"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    kpiAttribute = db.Column(
        db.Unicode(80),
        nullable=False
    )

    initiateDate = db.Column(
        db.Date,
        nullable=False
    )

    initiateMonth = db.Column(
        db.Unicode(80),
        nullable=False
    )

    initiateYear = db.Column(
        db.Unicode(80),
        nullable=False
    )


class Form(db.Model):
    __tablename__ = "Form"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    issueDate = db.Column(
        db.Date,
        nullable=False
    )
    noOfFormGenerate = db.Column(
        db.Integer,
        nullable=False
    )

class Comments(db.Model):
    __tablename__ = "Comments"
    __table_args__ = {

    }
    id = db.Column(
        db.Integer,
        primary_key=True
    )

