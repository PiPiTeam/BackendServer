from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_redis import FlaskRedis
from sqlalchemy import MetaData

MetaData(schema=["User"])
db = SQLAlchemy()
migrate = Migrate()
api = Api(prefix="/api")
redis = FlaskRedis()
