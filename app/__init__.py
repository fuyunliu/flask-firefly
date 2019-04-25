# -*- coding: utf-8 -*-
import pendulum
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from celery import Celery
from config import config, Config

db = SQLAlchemy()
mail = Mail()
sess = Session()

celery_app = Celery(__name__)
celery_app.config_from_object(Config, namespace='CELERY')

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def timesince(dt):
    return pendulum.instance(dt).diff_for_humans()


def create_app(config_name):
    app = Flask(__name__)
    app.jinja_env.auto_reload = True  # 静态资源修改不更新问题
    app.jinja_env.filters['timesince'] = timesince
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    sess.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
