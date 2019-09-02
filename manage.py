from flask import Flask, make_response
import settings
import views
from extensions import db, migrate, api, redis
from models import init_models
from collections import OrderedDict
from flask import make_response


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    # db
    db.init_app(app)
    migrate.init_app(app, db)

    # api
    views.init(api)
    api.init_app(app)

    redis.init_app(app)

    return app


app = create_app()

init_models()


def make_bad_response(response):
    data = OrderedDict({
        "code": 1,
        "message": "",
        "data": response.json['errors']
    })
    return make_response(data, response.status_code)


@app.after_request
def handler_response(response):
    if response.content_type == 'application/json' and 200 <= response.status_code <= 209:
        data = OrderedDict({
            "code": 0,
            "message": "成功",
            "data": response.json
        })
        return make_response(data, response.status_code)
