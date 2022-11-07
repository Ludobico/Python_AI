from flask import Flask
#pybo.py와 pybo/__init__.py는 동일한 pybo 모듈이다.
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(): #create_app 대신 다른 이름을 사용하면 정상적으로 동작하지 않는다.
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from .import models

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
