from extensions import db
from sqlalchemy_utils import Timestamp


class Feedback(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(128))
    subject = db.Column(db.String(128))
    message = db.Column(db.Text)


class Product(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.TEXT)
    price = db.Column(db.DECIMAL(14, 2))
    is_home = db.Column(db.Boolean, default=False)
    banners = db.relationship('ProductBanner')
    details = db.relationship('ProductDetail')
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))


class ProductBanner(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    url = db.Column(db.String(2048))


class ProductDetail(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    url = db.Column(db.String(2048))


class ProductCategory(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    products = db.relationship('Product', backref='category')
