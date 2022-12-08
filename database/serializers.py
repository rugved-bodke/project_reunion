from marshmallow import fields as ms_fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from database.models import Users, FollowingActivities, PostActivities, Posts
from uuid import UUID

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True

    id = ms_fields.String()
    username = ms_fields.String()
    email = ms_fields.String()
    password = ms_fields.String()

class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Posts
        include_relationships = True
        load_instance = True

    id = ms_fields.String()
    user_id = ms_fields.String()
    created_at = ms_fields.DateTime()
    title = ms_fields.String()
    description = ms_fields.String()

class FollowingActivitiesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FollowingActivities
        include_relationships = True
        load_instance = True

    id = ms_fields.String()
    user_id = ms_fields.String()
    type = ms_fields.String()
    activity_id = ms_fields.String()

class PostActivitiesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PostActivities
        include_relationships = True
        load_instance = True

    id = ms_fields.String()
    post_id = ms_fields.String()
    user_id = ms_fields.String()


