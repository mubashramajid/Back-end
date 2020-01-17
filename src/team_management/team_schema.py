from marshmallow import fields, Schema
from src.db import db
from src.app import marshmallow_app
from src.team_management.team_model import Team


class TeamSchema(marshmallow_app.ModelSchema):
    teamName=fields.String()


class Meta:
    model = Team,


team_schema = TeamSchema()