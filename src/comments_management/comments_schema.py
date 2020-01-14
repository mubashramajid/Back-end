from marshmallow import fields, Schema
from src.db import db
from src.app import marshmallow_app
from src.comments_management.comments_model import Comments


class CommentsSchema(marshmallow_app.ModelSchema):
    description=fields.String()


class Meta:
    model = Comments,


comments_schema = CommentsSchema()

