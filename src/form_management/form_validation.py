from marshmallow import fields,Schema, ValidationError, validates_schema, validate
import re


class FormValidation(Schema):

    issue_Date = fields.String(
        required=True,
        error_messages={"required": "Please mention issue date of the form."}
    )

    no_Of_Form_Generate = fields.String(
        required=True,
        error_messages={"required": "Please mention issue date of the form."}
    )
