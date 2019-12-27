from flask_restplus import Resource
from src.app import api
from src.employee_management.employee_validation import EmployeeValidation
from webargs.flaskparser import use_args

employee_namespace = api.namespace("employee", description="endpoints for Employee module")


@api.route('/employee/')
class EmployeesList(Resource):

    # get list of all employees
    def get(self):
        return {"message": "yes it is working"}
        pass

    # Create a new employee
    @use_args(EmployeeValidation())
    def post(self, form_data):
        return {"message": "validation was successful"} # please remove this line

        # 1. please check if the provided email and cnic number doesn't already exist
            # 1a. If it exists then we will return an error
            # first import db from src
            # then do this. result = db.session.query(Employee).filter(Employee.cnic == form_data["cnic"]
            # if it's not found it db, result will be None. `if result != None`:
            # e.g. return {"message": "this employee has already been added"}, 401

        # 1b. If the user doesn't exists then we will create a new user in db.
            # e.g. we will use/import `Employee` from employee_mode and we will create a instance of it.
            # new_employee = Employee(first_name=form_data["first_name"], .........)
            # return {"message": "new employee has been added successfully"}
        pass
