from marshmallow import Schema, fields


class LoginSchema(Schema):
    user_id = fields.String(required=True)
    password = fields.String(load_only=True, required=True)


