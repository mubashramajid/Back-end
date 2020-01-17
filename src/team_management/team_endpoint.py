from flask_restplus import Resource
from src.app import api
from src.team_management.team_validation import TeamValidation
from webargs.flaskparser import use_args
from src import db
from src.team_management.team_model import Team
from sqlalchemy import delete, update
from werkzeug.exceptions import HTTPException
import os


team_namespace = api.namespace("team", description="endpoints for team module")


@use_args(TeamValidation())
@api.route('/team/')
class TeamList(Resource):

    def get(self):
        get_data = db.session.query(Team).all()
        result = []
        for row in get_data:
            result.append(
                {"team_name": row.teamName,
                 "emp_id": row.employee_id
                }
            )
        return {"data": result}
        pass

    @use_args(TeamValidation())
    def post(self, form_data):
        new_team = Team(
            # teamName= "Review Genie"
            teamName= form_data["team_name"],
            employee_id = form_data["emp_id"]
        )
        db.session.add(new_team)
        db.session.commit()
        return {"message": "Team has been added successfully."}
        pass

@api.route('/team/<int:id>')
class TeamListAPI(Resource):

    @use_args(TeamValidation())
    def put(self,form_data, id):
        result = db.session.query(Team).filter(Team.id == id).update(
            {
                "teamName": form_data["team_name"],
                "employee_id" : form_data["emp_id"]
            }
        )
        db.session.commit()
        return {"message": "Team has been updated successfully."}
        pass
    

