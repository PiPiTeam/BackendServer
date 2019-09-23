from views.common import FeedbackView
from views.product import ProductView, ProductCategoryView


def init(api):
    api.add_resource(FeedbackView, '/feedback')
    api.add_resource(ProductView, '/products')
    api.add_resource(ProductCategoryView, '/product-categories')
    api.add_resource(ProductCategoryView, '/product-categories/<pk>', endpoint='ProductCategoryDetail')
