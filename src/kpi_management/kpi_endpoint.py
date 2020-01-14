from flask_restplus import Resource
from src.app import api
from src.kpi_management.kpi_validation import KPIValidation
from src.kpi_management.kpi_model import KPI
from src.kpi_management.kpi_schema import kpi_schema
from webargs.flaskparser import use_args
from src import db
from sqlalchemy import delete, update
from werkzeug.exceptions import HTTPException
import os


kpi_namespace = api.namespace("kpi", description="endpoints for kpi module")
@use_args(KPIValidation)
@api.route('/kpi/')
class KPIList(Resource):

    def get(self):
        get_data = db.session.query(KPI).all()
        result = []
        for row in get_data:
            result.append({"kpi_attribute": row.kpiAttribute,"initiate_date": row.initiateDate, "completion_month": row.completionMonth,"completion_year": row.completionYear,"status": row.status})
        return {"data": result}
        pass
