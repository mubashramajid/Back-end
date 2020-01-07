from marshmallow import Schema, fields, validates_schema, ValidationError, validate
from marshmallow_enum import EnumField
import re


class DepartmentValidation(Schema):

    first_name = fields.String(
        required=True,
        error_messages={"required": "Please enter First name."}
    )

    last_name = fields.String(
        required=True,
        error_messages={"required": "Please enter Last name."}
    )

    depart_Name = fields.String(
        required=True,
        error_messages={"required": "Please enter Department name."},
    )

    employee_Designation = fields.String(
        required=True,
        error_messages={"required": "Please enter Employee Designation."}
    )

    team_Name = fields.String(
        required=True,
        error_messages={"required": "Please enter Team name.."}
    )