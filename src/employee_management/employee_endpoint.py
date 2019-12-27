from flask_restplus import Resource
from src.app import api
from src.employee_management.employee_validation import EmployeeValidation
from webargs.flaskparser import use_args
from src import db
from src.employee_management.employee_model import Employee, EmployeeTypes


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
        #result = db.session.query(EmployeeValidation).filter() | or_() vs and_()
        result_cnic = db.session.query(Employee).filter(Employee.cnic == form_data["cnic"]).all()
        result_email = db.session.query(Employee).filter(Employee.email == form_data["email"]).all()
        # result_phone = db.session.query(Employee).filter(Employee.phonenumber == form_data["phonenumber"]).all()
        if len(result_cnic) != 0:
            return {"message": "The provided CNIC numner is already associated with some other employee."}, 401
        elif len(result_email) != 0:
            return {"message": "The provided Email Address is already associated with some other employee."}, 401
        # elif result_phone is not None:
        #     return {"message": "The The provided Phone number is already associated with some other employee."}, 401
        else:
            new_employee = Employee(
                firstName=form_data["first_name"],
                lastName=form_data["last_name"],
                email=form_data["email"],
                cnic=form_data["cnic"],
                # employee_type= EmployeeTypes.PROJECT_MANAGER,
                gender=form_data["gender"],
                # phonenumber=form_data["phonenumber"]
            )
            new_employee.password_hash = form_data["password"]
            db.session.add(new_employee)
            db.session.commit()
            return {"message": "Employee has been added successfully."}


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
