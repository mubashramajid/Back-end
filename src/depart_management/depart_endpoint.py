from flask_restplus import Resource
from src.app import api
from src.depart_management.depart_validation import DepartmentValidation
from webargs.flaskparser import use_args
from src import db
from src.depart_management.depart_model import Department
from sqlalchemy import delete, update
# from src.employee_management.employee_schema import employee_schema
from werkzeug.exceptions import HTTPException
import os

department_namespace = api.namespace("department", description="endpoints for team module")

@use_args(DepartmentValidation)
@api.route('/department/')
class DepartmentList(Resource):

    def get(self):
        get_data = db.session.query(Department).all()
        result = []
        for row in get_data:
            result.append({"depart_name": row.departName, "no_of_employee": row.noOfEmployee})
        return {"data": result}
        pass
