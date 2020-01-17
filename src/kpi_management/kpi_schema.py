from marshmallow import fields, Schema
from src.db import db
from src.app import marshmallow_app
from src.kpi_management.kpi_model import KPI


class KPISchema(marshmallow_app.ModelSchema):
    # kpi_name=fields.string()
    kpiAttribute=fields.String()
    initiateDate=fields.Date()
    completionDate=fields.Date()
    department_id = fields.String()
class Meta:
    model = KPI,


kpi_schema = KPISchema()
