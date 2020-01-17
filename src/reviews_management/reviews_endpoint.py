from flask_restplus import Resource
from src.app import api
from src.reviews_management.reviews_validation import ReviewsValidation
from webargs.flaskparser import use_args
from src import db
from src.reviews_management.reviews_model import Reviews
from sqlalchemy import delete, update
from src.reviews_management.reviews_schema import reviews_schema
# from src.employee_management.employee_schema import employee_schema
from werkzeug.exceptions import HTTPException
import os


reviews_namespace = api.namespace("reviews", description="endpoints for reviews module")

@use_args(ReviewsValidation())
@api.route('/review/')
class ReviewsList(Resource):

    def get(self):
        get_data = db.session.query(Reviews).all()
        result = []
        for row in get_data:
            result.append(
                {
                    "status": row.status,
                    "completion_Date": row.completionDate,
                    "initiate_Date": row.initiateDate,

                }
            )
        return {"data": result}
        pass

    @use_args(ReviewsValidation())
    def post(self,form_data):
        new_review = Reviews(
            initiateDate= form_data["initiate_Date"],
            completionDate= form_data["completion_Date"],
            status = form_data["status"]
        )
        db.session.add(new_review)
        db.session.commit()
        return {"message":"Review has been added successfully."}
        pass


@api.route('/review/<int:id>')
class ReviewListAPI(Resource):

    @use_args(ReviewsValidation())
    def put(self,form_data,id):
        result = db.session.query(Reviews).filter(Reviews == id).update(
            {
                "initiateDate" : form_data["initiate_Date"],
                "completionDate" : form_data["completion_Date"],
                "status" : form_data["status"]
            }
        )
        db.session.commit()
        return {"message": "Review has been updated successfully."}
        pass