from marshmallow import Schema, fields, validates_schema, ValidationError, validate
from marshmallow_enum import EnumField
import re


class DepartmentValidation(Schema):

    id = fields.Integer(

    )

    depart_name = fields.String(
        required=True,
        error_messages={"required": "Please enter Department name."}
    )

    # no_Of_Employee = fields.String(
    #     required=True,
    #     error_messages={"required": "Please enter No. of Employees in the Department."}
    # )

