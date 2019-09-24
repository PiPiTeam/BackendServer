import os
import time

from flask_restful import Resource, fields, marshal_with

from extensions import db
from models.admin import Feedback
from settings import FILE_DIR, FILE_SERVER_DOMAIN
from views.parsers.common import feedback_parser, file_upload_parser

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


class FileUploadView(Resource):

    def post(self):
        args = file_upload_parser.parse_args()
        file = args['file']
        filename = str(int(time.time() * 1000)) + os.path.splitext(file.filename)[1]
        file_path = os.path.join(FILE_DIR, filename)
        file.save(file_path)
        return {'url': FILE_SERVER_DOMAIN + '/images/' + filename}, 201
