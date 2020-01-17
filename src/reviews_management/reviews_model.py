from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Table,Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src import db
from flask_restplus import Resource
from src.app import api


class Reviews(db.Model):
    __tablename__ = "Reviews"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Reviews (Parent) table is Primary key for Form table - one to many RS
    # form = db.relationship('Form', back_populates="Reviews")

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
