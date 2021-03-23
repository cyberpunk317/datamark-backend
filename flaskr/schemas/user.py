from marshmallow import fields, Schema


class UserSchema(Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)
    num_mark_tasks = fields.Integer(required=True)
    registration_date = fields.Time(required=True)
    last_activity_date = fields.Time(required=False)
