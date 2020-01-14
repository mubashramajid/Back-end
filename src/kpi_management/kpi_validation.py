from marshmallow import fields,Schema, ValidationError, validates_schema, validate
import re


class KPIValidation(Schema):

    kpi_Attribute = fields.String(
        required=True,
        error_messages={"required": "Please enter KPI attribute."}
    )

    initiate_Date = fields.String(
        required=True,
        error_messages={"required": "Please mention the starting date."}
    )

    initiate_Month = fields.String(
        required=True,
        error_messages={"required": "Please mention the month."}
    )

    initiate_Year = fields.String(
        required=True,
        error_messages={"required": "Please mention the year."}
    )
