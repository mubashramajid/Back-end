from marshmallow import fields, Schema

from src.db import db
from src.app import marshmallow_app
from src.hr_management.depart_model import Department


class DepartmentSchema(marshmallow_app.ModelSchema):
    # first_name = fields.String()
    # last_name = fields.String()
    # cnic = fields.String()
    # gender = fields.Boolean()
    # email = fields.Email()
    # phonenumber = fields.String()

    class Meta:
        model = Department,


depart_schema = DepartmentSchema()
