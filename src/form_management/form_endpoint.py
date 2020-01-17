from flask_restplus import Resource
from src.app import api
from src.form_management.form_validation import FormValidation
from webargs.flaskparser import use_args
from src import db
from src.form_management.form_model import Form
from sqlalchemy import delete, update
from src.form_management.form_schema import form_schema
from werkzeug.exceptions import HTTPException
import os


form_namespace = api.namespace("form", description="endpoints for form module")

@use_args(FormValidation())
@api.route('/form/')
class FormList(Resource):

    def get(self):
        get_data = db.session.query(Form).all()
        result = []
        for row in get_data:
            result.append(
                {
                    "issue_Date": row.issueDate,
                    "no_Of_Form_Generate": row.noOfFormGenerate,
                    "emp_id": row.employee_id,
                    "rev_id": row.review_id
                }
            )
        return {"data": result}
        pass


    @use_args(FormValidation())
    def post(self, form_data):
        new_form = Form(
            issueDate= form_data["issue_Date"],
            noOfFormGenerate= form_data["no_Of_Form_Generate"],
            employee_id= form_data["emp_id"],
            review_id=form_data["rev_id"]
        )
        db.session.add(new_form)
        db.session.commit()
        return {"message": "Form has been added successfully."}
        pass

@api.route('/form/<int:id>')
class FormListAPI(Resource):

    @use_args(FormValidation())
    def put(self,form_data, id):
        result = db.session.query(Form).filter(Form == id).update(
            {
                    "issueDate": form_data["issue_Date"],
                    "noOfFormGenerate": form_data["no_of_Form_Generate"],
                    "employee_id" : form_data["emp_id"],
                    "review_id" : form_data["rev_id"]
            }
        )
        db.session.commit()
        return{"message": "Form has been updated successfully."}
        passs