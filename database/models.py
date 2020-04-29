# models.py contains all of the declarative models for our database.
#
# docs => https://docs.sqlalchemy.org/en/13/orm/tutorial.html


import sqlalchemy
import sqlalchemy.ext.declarative as sqlalchemy_declarative
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func


# docs => https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping
Base = sqlalchemy_declarative.declarative_base()


class User(Base):
    __tablename__ = "users"

    # autogenerated fields
    id = Column(Integer, primary_key=True)

    # standard fields
    email = Column(String, nullable=False, default="")
    role = Column(String, nullable=False, default="")
    familyName = Column(String, nullable=False, default="")
    givenName = Column(String, nullable=False, default="")
    smsUser = Column(Boolean, nullable=False, default=True)
    createTime = Column(DateTime, default=func.now())
    lastModified = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<User({self.email}, {self.role})>"
