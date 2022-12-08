from marshmallow import fields as ms_fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from database.models import Users

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True

    id = ms_fields.String()
    username = ms_fields.String()
    email = ms_fields.String()
    password = ms_fields.String()