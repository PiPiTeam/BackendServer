from views.common import FeedbackView
from views.product import ProductView


def init(api):
    api.add_resource(FeedbackView, '/feedback')
    api.add_resource(ProductView, '/product')
