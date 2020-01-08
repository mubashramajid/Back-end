from flask_restplus import Resource
from src.app import api
from src.depart_management.depart_validation import DepartmentValidation, EmployeeValidationUpdate
from webargs.flaskparser import use_args
from src import db
from src.depart_management.depart_model import Department
from sqlalchemy import delete, update
# from src.employee_management.employee_schema import employee_schema
from werkzeug.exceptions import HTTPException
import os

employee_namespace = api.namespace("employee", description="endpoints for Employee module")


@api.route('/department/')
class DepartmentList(Resource):
    # get list of all employees
    def get(self):
        get_data = db.session.query(Department).all()
        result = []
        for row in get_data:
            result.append({"first_name": row.firstName, "last_name": row.lastName, "depart_Name": row.departName, "employee_Designation": row.employeeDesignation, "team_Name": row.teamName})
        # result = employee_schema.dump(get_data)
        return {"data": result}
        # return {"message": "yes it is working"}
        pass
