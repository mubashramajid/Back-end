from flask_restplus import Resource
from src.app import api
from src.team_management.team_validation import TeamValidation
# from src.depart_management.depart_validation import DepartmentValidation
from webargs.flaskparser import use_args
from src import db
from src.team_management.team_model import Team
from sqlalchemy import delete, update
from werkzeug.exceptions import HTTPException
import os


team_namespace = api.namespace("team", description="endpoints for team module")


@api.route('/team/')
@use_args(TeamValidation())
class TeamList(Resource):

    def get(self):
        get_data = db.session.query(Team).all()
        result = []
        for row in get_data:
            result.append({"team_name": row.teamName, "team_members": row.teamMembers})
        return {"data": result}
        pass
