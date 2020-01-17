from flask_restplus import Resource
from src.app import api
from src.employee_management.employee_validation import EmployeeValidation, EmployeeValidationUpdate
from webargs.flaskparser import use_args
from src import db
from src.employee_management.employee_model import Employee, EmployeeTypes
from sqlalchemy import delete, update
# from src.employee_management.employee_schema import employee_schema
from werkzeug.exceptions import HTTPException
import os

employee_namespace = api.namespace("employee", description="endpoints for Employee module")


@api.route('/employee/')
class EmployeesList(Resource):
    # get list of all employees
    def get(self):
        # from src.employee_management import employee_schema
        # from src.employee_management.employee_schema import EmployeeSchema
        # get_data = db.session.query(Employee).filter(Employee.department_id == id).all()
        get_data = db.session.query(Employee).all()
        result = []
        for row in get_data:
            result.append({"first_name": row.firstName, "last_name": row.lastName, "gender": row.gender})
        # result = employee_schema.dump(get_data)
        return {"data": result}
        # return {"message": "yes it is working"}
        pass

    # Create a new employee
    @use_args(EmployeeValidation())
    def post(self, form_data):
        # result = db.session.query(EmployeeValidation).filter() | or_() vs and_()
        result_cnic = db.session.query(Employee).filter(Employee.cnic == form_data["cnic"]).all()
        result_email = db.session.query(Employee).filter(Employee.email == form_data["email"]).all()
        result_phone = db.session.query(Employee).filter(Employee.phonenumber == form_data["phonenumber"]).all()
        if len(result_cnic) != 0:
            return {"message": "The provided CNIC numner is already associated with some other employee."}, 401
        elif len(result_email) != 0:
            return {"message": "The provided Email Address is already associated with some other employee."}, 401
        elif len(result_phone) != 0:
            return {"message": "The The provided Phone number is already associated with some other employee."}, 401
        else:
            new_employee = Employee(

                firstName=form_data["first_name"],
                lastName=form_data["last_name"],
                email=form_data["email"],
                cnic=form_data['cnic'],
                employee_type=form_data["employee_type"],
                gender=form_data["gender"],
                phonenumber=form_data["phonenumber"],
                designation = form_data["designation"],
                joinDate = form_data["join_Date"],
                leaveDate = form_data["leave_Date"],
                department_id = form_data["depart_id"]
            )

            # news_employee = "INSERT INTO `opine_cue`.`employee`(`firstName`, `lastName`, `email`, `password`, `gender`, `designation`,`cnic`, `phonenumber`)
            # VALUES(form_data['depart_id'],form_data['first_name'],form_data['last_name'] , form_data['email'],form_data['password'],form_data['confirm_password'],form_data['gender'], form_data['designation'],form_data['cnic'] ,form_data['phonenumber']);"
            # print(new_employee);

            # VALUES(form_data['2'], form_data['4'], form_data['adf'], form_data['adf'], form_data['asad@gmail.com'],
            #        form_data['132'], form_data['1'], form_data['EMPLOYEE'], form_data['4210547896541'],
            #        form_data['+9214789654210']);
            # "

            new_employee.password_hash = form_data["password"]
            db.session.add(new_employee)
            db.session.commit()
            return {"message": "Employee has been added successfully."}
            pass


@api.route('/employee/<int:id>')
class EmployeelistAPI(Resource):
    def get(self, id):
        # result = db.session.query(Employee).filter(Employee.id == id).first()
        # return {"result": {"first_name": result, "last_name": result, "email": result, "cnic": result,
        #                    "employee_type": result, "gender": result, "phonenumber": result, "designation": result}}
        # return {id: result}

        # print(result)
        # return{"result": {
        #     result : "first_name"
        # }}

        result = db.session.query(Employee).filter(Employee.id == id)
        api_result = {}
        for row in result:
            api_result[str(row.str)] = {
                "firstName": row.firstName,
                "lastName": row.lastName,
                "cnic": row.cnic,
                "gender": row.gender,
                "phonenumber": row.phonenumber,
                "department_id": row.department_id,
                "joinDate": row.joinDate,
                "leaveDate": row.leaveDate,
                "email": row.email,
                "designation": row.designation,
                "employee_type": row.employee_type
            }

            return api_result

    # Update an existing Employee
    @use_args(EmployeeValidationUpdate())
    def put(self, form_data, id):

        result = db.session.query(Employee).filter(Employee.id == id).first()

        result.firstName = form_data["first_name"],
        result.lastName = form_data["last_name"],
        # result.email = "mubashra123@gmail.com",
        result.cnic = form_data["cnic"],
        result.employee_type = form_data["employee_type"],
        result.gender = form_data["gender"],
        result.phonenumber = form_data["phonenumber"],
        result.designation = form_data["designation"],
        result.joinDate = form_data["join_Date"],
        result.leaveDate = form_data["leave_Date"]
        db.session.add(result)
        db.session.commit()

    # delete and existing entry

    def delete(self, id):
        try:
            if db.session.query(Employee).filter(Employee.id == id).delete() is not None:
                # db.session.query(Employee).filter(Employee.id == id).delete()
                return {"messages", "Employee removed successfully"}
            else:
                return {'id not found'}

        except HTTPException as error:

            return {"message", "id not found"}

# api.add_resource(EmployeesList,'/employee/tasks' , endpoint='tasks')
# api.add_resource(EmployeelistAPI,'/emloyee/tasks/<int:id>' , endpoit='task')

# @api.route("/dashboard" ,method=['GET', 'POST'])
# def dashboard():
#     if request.method=='POST':
#         email =request.form.get('email')
#         password=request.form.get('password')