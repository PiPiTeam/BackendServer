from flask_restful.reqparse import RequestParser

feedback_parser = RequestParser(bundle_errors=True)
feedback_parser.add_argument("username", type=str, required=True, nullable=False)
feedback_parser.add_argument("email", type=str, required=True, nullable=False)
feedback_parser.add_argument("subject", type=str, required=True, nullable=False)
feedback_parser.add_argument("message", type=str, required=True, nullable=False)
