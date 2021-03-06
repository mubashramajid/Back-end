from marshmallow import fields,Schema, ValidationError, validates_schema, validate
import re


class ReviewsValidation(Schema):

    initiate_Date = fields.Date(
        required=True,
        error_messages={"required": "Please enter Review Initiate Date."}
    )

    completion_Date = fields.Date(
        required=True,
        error_messages={"required": "Please enter Review Completion Date."}
    )

    status = fields.Boolean(
        required=True,
        error_messages={"required": "Please mention Review Status."}
    )
