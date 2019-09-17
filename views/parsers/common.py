from decimal import Decimal

from flask_restful.reqparse import RequestParser

feedback_parser = RequestParser(bundle_errors=True)
feedback_parser.add_argument("username", type=str, required=True, nullable=False)
feedback_parser.add_argument("email", type=str, required=True, nullable=False)
feedback_parser.add_argument("subject", type=str, required=True, nullable=False)
feedback_parser.add_argument("message", type=str, required=True, nullable=False)

product_banner_parser = RequestParser(bundle_errors=True)
product_banner_parser.add_argument("name", type=str, required=True, nullable=False)

product_parser = RequestParser(bundle_errors=True)
product_parser.add_argument("name", type=str, required=True, nullable=False)
product_parser.add_argument("description", type=str, required=True, nullable=False)
product_parser.add_argument("price", type=Decimal, required=True, nullable=False)
product_parser.add_argument("is_home", type=bool, required=False, nullable=False)
