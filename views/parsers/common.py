from decimal import Decimal

from flask_restful import inputs
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
product_parser.add_argument("category_id", type=int, required=True, nullable=False)
product_parser.add_argument("description", type=str, required=True, nullable=False)
product_parser.add_argument("price", type=Decimal, required=True, nullable=False)
product_parser.add_argument("banners", type=str, action='append', required=True, nullable=False)
product_parser.add_argument("details", type=str, action='append', required=True, nullable=False)
product_parser.add_argument("is_home", type=bool, required=False, nullable=False)

product_category_parser = RequestParser(bundle_errors=True)
product_category_parser.add_argument("name", type=str, required=True, nullable=False)

product_query_parser = RequestParser(bundle_errors=True)
product_query_parser.add_argument("name", type=str, required=False, location='values')
product_query_parser.add_argument("category_name", type=str, required=False, location='values')
product_query_parser.add_argument("is_home", type=inputs.boolean, required=False, location='values')
