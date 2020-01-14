from marshmallow import fields, Schema
from src.db import db
from src.app import marshmallow_app
from src.employee_management.employee_model import Employee


class EmployeeSchema(marshmallow_app.ModelSchema):
    first_name = fields.String()
    last_name = fields.String()
    cnic = fields.String()
    gender = fields.Boolean()
    email = fields.Email()
    phonenumber = fields.String()

class Meta:
    model = Employee,


employee_schema = EmployeeSchema()
