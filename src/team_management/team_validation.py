from marshmallow import fields,Schema, ValidationError, validates_schema, validate
import re

class TeamValidation(Schema):

    team_name = fields.String(
        required=True,
        error_messages={"required": "Please enter the Team name."}
    )
    emp_id = fields.String(
        required= True,
        error_messages={"required":"Please enter Employee ID."}
    )




    # teamMembers = fields.String(
    #     required=True,
    #     error_messages={"required": "Please enter no. of team members."}
    # )

