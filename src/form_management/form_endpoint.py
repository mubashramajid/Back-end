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
            result.append({"issue_date": row.issueDate,"no_of_form_generate": row.noOfFormGenerate})
        return {"data": result}
        pass
