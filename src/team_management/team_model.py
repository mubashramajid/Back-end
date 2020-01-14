from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Table,Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
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

    #Team (child) table is foreign key for Employee Table - many to one RS
    employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'))


    teamName = db.Column(
        db.Unicode(80),
        nullable=False
    )

    # teamMembers = db.Column(
    #     db.Integer,
    #     nullable=False
    # )

