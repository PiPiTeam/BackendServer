from flask_restful import Resource, fields, marshal_with

from extensions import db
from models.admin import Feedback
from views.parsers.common import feedback_parser

feedback_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'subject': fields.String,
    'message': fields.String
}


class FeedbackView(Resource):

    @marshal_with(feedback_fields)
    def get(self):
        instances = Feedback.query.limit(10).all()
        return instances

    @marshal_with(feedback_fields)
    def post(self):
        args = feedback_parser.parse_args()
        instance = Feedback(**args)
        db.session.add(instance)
        db.session.commit()
        return instance, 201
