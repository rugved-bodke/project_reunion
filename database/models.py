from datetime import date, datetime
from sqlalchemy import (
    JSON,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    Time,
    null,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid

Base = declarative_base()
metadata = Base.metadata


class Users(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    # followers = relationship("FollowingActivities", backref="users")
    # followings = relationship("PostActivities", backref="users")
    # posts = relationship("Posts", backref="users")


class Posts(Base):
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True,)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    # likes = relationship("PostActivities", backref="posts")
    # comments = relationship("Comments", backref="posts")


class FollowingActivities(Base):
    __tablename__ = "following_activities"
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    type = Column(String(64), nullable=False)
    other_user_id = Column(ForeignKey("users.id"), nullable=False)

class PostActivities(Base):
    __tablename__ = "post_activities"
    id = Column(UUID(as_uuid=True), primary_key=True)
    post_id = Column(ForeignKey("posts.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    type = Column(String(64), nullable=False)
    comment = Column(JSON, nullable=True)
