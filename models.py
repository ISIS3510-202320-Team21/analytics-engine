from database import Base, metadata
from sqlalchemy import Table

class User(Base):
    __table__ = Table("users", metadata)

class Notification(Base):
    __table__ = Table("notifications", metadata)

class Match(Base):
    __table__ = Table("matches", metadata)

class Sport(Base):
    __table__ = Table("sports", metadata)