from flask import request
from flask_restplus import Resource
from src.app import api
from src.kpi_management.kpi_validation import KPIValidation
from src.kpi_management.kpi_model import KPI
from src.kpi_management.kpi_schema import kpi_schema
from webargs.flaskparser import use_args
from src import db
from sqlalchemy import delete, update
from werkzeug.exceptions import HTTPException
import os
import json

kpi_namespace = api.namespace("kpi", description="endpoints for kpi module")

@use_args(KPIValidation)
@api.route('/kpi/')
class KPIList(Resource):

    def get(self):
        get_data = db.session.query(KPI).all()
        result = []
        for row in get_data:
            result.append({"kpi_attribute": row.kpiAttribute})
            # , "initiate_Date": row.initiateDate, "completion_Date": row.completionDate
        return {"data": result}
        pass

    @use_args(KPIValidation())
    def post(self, form_data):
        new_kpi = KPI(
            kpiAttribute= form_data["kpi_attribute"],
            initiateDate= form_data["initiate_Date"],
            completionDate = form_data["completion_Date"],
            department_id = form_data["depart_id"]
        )
        db.session.add(new_kpi)
        db.session.commit()
        return{"message": "KPI has been added successfully."}
        pass

@api.route('/kpi/<string:str>')
class KPIlistAPI(Resource):
        def get(self, str):
            # result = db.session.query(KPI).filter(KPI.department_id == str)
            result = db.session.query(KPI).filter(KPI.department_id.like( "%" + str + "%")).all()
            api_result = []
            for row in result:
                api_result.append(
                    { "kpiAttribute": row.kpiAttribute,
                      # "initiateDate": row.initiateDate,
                      # "completionDate": row.completionDate,
                      # "department_id": row.department_id
                    }
                )
            # result = employee_schema.dump(get_data)
            return {"data": api_result}
            # return {"message": "yes it is working"}
            pass


            # api_result = {}
            # for row in result:
            #     api_result[str(row.str)] = {
            #         "kpiAttribute": row.kpiAttribute,
            #         "initiateDate": row.initiateDate,
            #         "completionDate": row.completionDate,
            #         "department_id": row.department_id
            #     }
            #     return api_result
            #


            # get_data = db.session.query(KPI).filter(KPI.department_id.like( "%" + int(str) + "%")).all()
            # print(str)
            # get_data = db.session.query(KPI).filter(KPI.department_id.like("%2%")).all()

            #  get_data = db.session.query(KPI).filter(KPI.department_id == str ).all()
            #  get_data = db.session.query(KPI).filter(KPI.department_id.contains(request.args.get(str)))
            # return {str: get_data}


            # result = []
            # for row in get_data:
            #     result.append({"kpi_attribute": row.kpiAttribute})
            #     # , "initiate_Date": row.initiateDate, "completion_Date": row.completionDate
            # return {"data": result}
            # pass

            # retrun { str :}

            # return json.dumps(get_data), 200, {
            #       'content-type': 'application/json'}

            # return {get_data : "kpiAttribute"}
            # return {
            #     "result":
            #     {
            #     kpiAttribute: "depart_name"
            #     }
            # }
