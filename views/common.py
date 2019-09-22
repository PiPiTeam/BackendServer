from flask_restful import Resource, fields, marshal_with

from extensions import db
from models.admin import Feedback
from views.parsers.common import feedback_parser

feedback_fields = {
    'created': fields.DateTime(dt_format='iso8601'),
    'updated': fields.DateTime(dt_format='iso8601'),
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'subject': fields.String,
    'message': fields.String
}


def pagination_fields(items_fields):
    return {
        'has_next': fields.Boolean,
        'has_prev': fields.Boolean,
        'items': fields.Nested(items_fields),
        'next_num': fields.Integer,
        'page': fields.Integer,
        'pages': fields.Integer,
        'per_page': fields.Integer,
        'prev_num': fields.Integer
    }


class FeedbackView(Resource):

    @marshal_with(pagination_fields(feedback_fields))
    def get(self):
        pagination = Feedback.query.paginate()
        return pagination

    @marshal_with(feedback_fields)
    def post(self):
        args = feedback_parser.parse_args()
        instance = Feedback(**args)
        db.session.add(instance)
        db.session.commit()
        return instance, 201
