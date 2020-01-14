from flask_restplus import Resource
from src.app import api
from src.comments_management.comments_validation import CommentsValidation
from src.comments_management.comments_model import Comments
from webargs.flaskparser import use_args
from src import db
from sqlalchemy import delete, update
from src.comments_management.comments_schema import comments_schema
from werkzeug.exceptions import HTTPException
import os


comments_namespace = api.namespace("comments", description="endpoints for comment module")

@api.route('/Comments/')
class CommentsList(Resource):

    def get(self):
        get_data = db.session.query(Comments).all()
        result = []
        for row in get_data:
            result.append({"issue_date": row.issueDate,"no_of_form_generate": row.noOfFormGenerate})
        return {"data": result}
        pass