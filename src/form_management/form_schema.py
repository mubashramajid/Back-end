from marshmallow import fields, Schema
from src.db import db
from src.app import marshmallow_app
from src.form_management.form_model import Form

class FormSchema(marshmallow_app.ModelSchema):
    # id=fields.String()
    issueDate=fields.String()
    noOfFormGenerate=fields.String()

class Meta:
    model = Form,


form_schema = FormSchema()