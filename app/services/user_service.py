# app/services/user_service.py
from ..models import User
from ..extensions import db

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

# app/services/tracker_service.py
from ..models import Tracker, TrackerEntry
from ..extensions import db
from flask_login import current_user

def create_tracker(name, description):
    tracker = Tracker(
        name=name, 
        description=description, 
        user_id=current_user.id
    )
    db.session.add(tracker)
    db.session.commit()
    return tracker

def add_tracker_entry(tracker_id, value, note=None):
    entry = TrackerEntry(
        tracker_id=tracker_id, 
        value=value, 
        note=note
    )
    db.session.add(entry)
    db.session.commit()
    return entry
