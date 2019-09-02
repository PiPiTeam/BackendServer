from views.common import FeedbackView


def init(api):
    api.add_resource(FeedbackView, '/feedback')
