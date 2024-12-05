from flask import Flask
from app.blueprints.user import user
from app.blueprints.web_user import web_user
from app.blueprints.website import create,read,update,delete

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()

def create_app():
    
        
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./testdb.db'

    db.init_app(app)

    #app.secret_key
    app.register_blueprint(user.bp)
    app.register_blueprint(web_user.bp)
    app.register_blueprint(create.bp)
    app.register_blueprint(update.bp)
    app.register_blueprint(read.bp)
    app.register_blueprint(delete.bp)

    migrate=Migrate(app,db)

    return app
