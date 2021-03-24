from marshmallow import fields, Schema


class UserSchema(Schema):
    user_id = fields.Integer(required=True)
    name = fields.String(required=True)
    password = fields.String(required=True)
    num_mark_tasks = fields.Integer(required=False)
    registration_date = fields.Time(required=False)
    last_activity_date = fields.Time(required=False)
