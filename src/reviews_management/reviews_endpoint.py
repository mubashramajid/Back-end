from flask_restplus import Resource
from src.app import api
from src.reviews_management.reviews_validation import ReviewsValidation
from webargs.flaskparser import use_args
from src import db
from src.reviews_management.reviews_model import Reviews
from sqlalchemy import delete, update
# from src.employee_management.employee_schema import employee_schema
from werkzeug.exceptions import HTTPException
import os


reviews_namespace = api.namespace("reviews", description="endpoints for reviews module")
@use_args(ReviewsValidation())
@api.route('/reviews/')
class ReviewsList(Resource):

    def get(self):
        get_data = db.session.query(Reviews).all()
        result = []
        for row in get_data:
            result.append({"initiate_date": row.initiateDate, "completion_date": row.completionDate,"status": row.status})
        return {"data": result}
        pass

