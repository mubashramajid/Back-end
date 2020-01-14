from marshmallow import fields, Schema

from src.db import db
from src.app import marshmallow_app
from src.depart_management.depart_model import Department


class DepartmentSchema(marshmallow_app.ModelSchema):
    # id=fields.String()
    departName=fields.String()

class Meta:
     model = Department,


department_schema = DepartmentSchema()
