from marshmallow import fields,Schema, ValidationError, validates_schema, validate
import re

class TeamValidation(Schema):

    teamName = fields.String(
        required=True,
        error_messages={"required": "Please enter the team name."}
    )

    teamMembers = fields.String(
        required=True,
        error_messages={"required": "Please enter no. of team members."}
    )
