from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Table,Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src import db
from flask_restplus import Resource
from src.app import api


class KPI(db.Model):
    __tablename__ = "KPI"
    __table_args__ = {

    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # KPI (Parent) table is primary key of Comment table - one to many RS
    comments = db.relationship("Comments", back_populates="KPI")


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
