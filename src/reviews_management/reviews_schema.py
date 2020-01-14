from marshmallow import fields, Schema
from src.db import db
from src.app import marshmallow_app
from src.reviews_management.reviews_model import Reviews


class ReviewsSchema(marshmallow_app.ModelSchema):
    initiateDate=fields.Date()
    completionDate=fields.Date()
    status=fields.Boolean()
class Meta:
    model = Reviews,


reviews_schema = ReviewsSchema()

