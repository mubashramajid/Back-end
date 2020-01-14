from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Table,Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src import db
from flask_restplus import Resource
from src.app import api


class Comments(db.Model):
    __tablename__ = "Comments"
    __table_args__ = {

    }
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    description = db.Column(
        db.Unicode(80),
        nullable=False
    )

    # Comments (Child) table is Foriegn key for Form table - many to one RS
    form_id = db.Column(db.Integer, db.ForeignKey('Comments.id'))

    # Comemnts (child) table is Foriegn key for KPI table - many to one Rs
    kpi_id = db.Column(db.Integer, db.ForeignKey('KPI.id'))


