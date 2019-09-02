from extensions import db
from sqlalchemy_utils import Timestamp


class Feedback(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(128))
    subject = db.Column(db.String(128))
    message = db.Column(db.Text)
