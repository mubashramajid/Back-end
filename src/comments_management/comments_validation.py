from marshmallow import fields,Schema, ValidationError, validates_schema, validate
import re


class CommentsValidation(Schema):

    description = fields.String(
        required=True,
        error_messages={"required": "Please enter comment for the Employee." }
    )