from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Table,Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src import db
from flask_restplus import Resource
from src.app import api



class Form(db.Model):
    __tablename__ = "Form"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Form (Parent) table is Primary key for Comment table - One to many RS
    comments = db.relationship('Comments', back_populates="Form")

    # Form (child) table is foreign key for Employee Table - many to one RS
    employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'))

    # Form (child) table is foreign key for Review Table - many to one RS
    review_id = db.Column(db.Integer, db.ForeignKey('Form.id'))

    issueDate = db.Column(
        db.Date,
        nullable=False
    )
    noOfFormGenerate = db.Column(
        db.Integer,
        nullable=False
    )
