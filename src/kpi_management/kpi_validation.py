from marshmallow import fields,Schema, ValidationError, validates_schema, validate
import re


class KPIValidation(Schema):

    kpi_Attribute = fields.String(
        required=True,
        error_messages={"required": "Please enter KPI attribute."}
    )

    initiate_Date = fields.Date(
        required=True,
        error_messages={"required": "Please mention the starting date."}
    )

    completion_Date = fields.Date(
        required=True,
        error_messages={"required": "Please mention the month."}
    )
    department_id = fields.String(
        required=True,
        error_messages={"required": "Please enter Deparment ID."}
    )