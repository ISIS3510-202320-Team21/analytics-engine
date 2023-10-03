from models import User, Notification, Match, Sport
from database import db
import datetime

def get_notifications_of_user(user_id: int):
    return db.query(Notification).filter(Notification.owner_id == user_id).all()

def get_user(user_id: int):
    return db.query(User).get(user_id)

#get all sports
def get_all_sports():
    return db.query(Sport).all()

#get the id of all users
def get_all_users():
    return db.query(User).all()

#get matches of a user
def get_matches_of_user(user_id: int):
    return db.query(Match).filter(Match.user_created_id == user_id).all()

#create notification for user
def create_user_notification(name: str, type: str, redirectTo: str, user_id: int):
    creationDate = datetime.datetime.now()
    seen = False
    db_notification = Notification(name=name, type=type, redirectTo=redirectTo, creationDate=creationDate, seen=seen, owner_id=user_id)
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification