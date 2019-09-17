from flask import request
from flask_restful import Resource, marshal_with, fields, abort

from extensions import db
from models.admin import Product, ProductBanner, ProductDetail
from views.parsers.common import product_parser

product_banner_fields = {
    'url': fields.String,
}

product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'is_home': fields.Boolean,
    'banners': fields.Nested(product_banner_fields),
    'details': fields.Nested(product_banner_fields),
}


class ProductView(Resource):

    @marshal_with(product_fields)
    def get(self):
        instances = Product.query.limit(10).all()
        return instances

    @marshal_with(product_fields)
    def post(self):
        args = product_parser.parse_args()
        banners = request.json.pop('banners', None)
        details = request.json.pop('details', None)
        product = Product(**args)
        db.session.add(product)
        db.session.flush()
        if not banners or not details:
            abort(400, message="参数错误")
        for banner in banners:
            product_banner = ProductBanner(product_id=product.id, url=banner['url'])
            db.session.add(product_banner)
        for detail in details:
            product_detail = ProductDetail(product_id=product.id, url=detail['url'])
            db.session.add(product_detail)
        db.session.commit()
        return product
