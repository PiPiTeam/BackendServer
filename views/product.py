from flask_restful import Resource, marshal_with, fields, abort, marshal

from extensions import db
from models.admin import Product, ProductBanner, ProductDetail, ProductCategory
from views.common import pagination_fields
from views.parsers.common import product_parser, product_category_parser, product_query_parser

product_banner_fields = {
    'url': fields.String,
}

product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'is_home': fields.Boolean,
    'banners': fields.List(fields.String(attribute='url')),
    'details': fields.List(fields.String(attribute='url')),
    'category_id': fields.Integer,
    'category_name': fields.String(attribute='category.name')
}

product_category_fields = {
    'id': fields.Integer,
    'name': fields.String
}


class ProductView(Resource):

    @marshal_with(pagination_fields(product_fields))
    def get(self):
        queryset = db.session.query(Product).order_by(Product.id.desc())
        args = product_query_parser.parse_args()
        name = args['name']
        if name:
            queryset = queryset.filter_by(name=name)
        category_name = args['category_name']
        if category_name:
            queryset = queryset.join(ProductCategory).filter(ProductCategory.name == category_name)
        is_home = args['is_home']
        if is_home:
            queryset = queryset.filter_by(is_home=is_home)
        pagination = queryset.paginate()
        return pagination

    @marshal_with(product_fields)
    def post(self):
        args = product_parser.parse_args()
        banners = args.pop('banners', None)
        details = args.pop('details', None)
        if not banners or not details:
            abort(400, message="参数错误")
        product = Product(**args)
        for url in banners:
            product.banners.append(ProductBanner(url=url))
        for url in details:
            product.details.append(ProductDetail(url=url))
        db.session.add(product)
        db.session.commit()
        return product


class ProductCategoryView(Resource):

    def get(self, pk=None):
        if pk:
            instance = ProductCategory.query.get_or_404(pk)
            return marshal(instance, product_category_fields)
        pagination = ProductCategory.query.paginate()
        return marshal(pagination, pagination_fields(product_category_fields))

    @marshal_with(product_category_fields)
    def post(self):
        args = product_category_parser.parse_args()
        if ProductCategory.query.filter_by(**args).one_or_none():
            abort(400, message="分类已存在")
        category = ProductCategory(**args)
        db.session.add(category)
        db.session.commit()
        return category

    @marshal_with(product_category_fields)
    def put(self, pk):
        instance = ProductCategory.query.get_or_404(pk)
        args = product_category_parser.parse_args()
        instance.name = args['name']
        db.session.add(instance)
        db.session.commit()
        return instance
