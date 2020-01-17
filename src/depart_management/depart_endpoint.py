from flask_restplus import Resource
from src.app import api
from src.depart_management.depart_validation import DepartmentValidation
from webargs.flaskparser import use_args
from src import db
from src.depart_management.depart_model import Department
from sqlalchemy import delete, update
from werkzeug.exceptions import HTTPException
import os

department_namespace = api.namespace("department", description="endpoints for department module")

@use_args(DepartmentValidation)
@api.route('/department/')
class DepartmentList(Resource):

    def get(self):
        get_data = db.session.query(Department).all()
        result = []
        for row in get_data:
            result.append(
                {"depart_name": row.departName}
            )
        return {"data": result}
        pass

# Create a new Department
    @use_args(DepartmentValidation())
    def post(self, form_data):
        # result = db.session.query(EmployeeValidation).filter() | or_() vs and_()
            new_depart = Department(
                departName=form_data["depart_name"]
            )
            db.session.add(new_depart)
            db.session.commit()
            return {"message": "Department has been added successfully."}
            pass


@api.route('/department/<int:id>')
class DepartmentlistAPI(Resource):
    def get(self, id):
        result = db.session.query(Department).filter(Department.id == id).first()
        # return {"result": {"first_name": result, "last_name": result, "email": result, "cnic": result,
        #                    "employee_type": result, "gender": result, "phonenumber": result, "designation": result}}
        return{"result": {
            result : "depart_name"
        }}
    # Update an existing Department
    @use_args(DepartmentValidation())
    def put(self, form_data, id):
        # result = db.session.query(Department).filter(Department.id == 1).update({"departName": "AI Department"})
        result = db.session.query(Department).filter(Department.id == id).update({"departName": form_data["depart_name"]})
        # result.departName = form_data["depart_name"],
        # result.departName = "AI Department",
        # db.session.add(result)
        db.session.commit()
        return {"message": "Department has been updated successfully."}
        pass
    # delete and existing entry

# sql alchemeny call get

    # def delete(self, id):
    #     try:
    #         if db.session.query(Department).filter(Department.id == id).delete():
    #             return {"messages": "Department removed successfully"}
    #         else:
    #             return {"message":"id not found"}
    #
    #     except HTTPException as error:
    #
    #         return {"message": "id not found."}

    # def delete(self, id):
    #
    #         delete =  Department.query.filter_by(id = id).first()
    #         db.session.delete(delete)
    #         db.session.commit()
    #         return {"message": "Department removed sucessfylly."}

    # def delete(self, id):
    #     try:
    #         if Department.query.filter_by(Department.id == id).first():
    #             db.session.delete()
    #             return {"messages": "Department removed successfully"}
    #         else:
    #             return {"message":"id not found"}
    #
    #     except HTTPException as error:
    #
    #         return {"message": "id not found."}
