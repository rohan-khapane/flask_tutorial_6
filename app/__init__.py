# from flask import Flask
# from app.blueprints.user import user
# from app.blueprints.web_user import web_user
# from app.blueprints.website import create,read,update,delete

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db=SQLAlchemy()

# app=Flask(__name__)
# #app.secret_key
# app.register_blueprint(user.bp)
# app.register_blueprint(web_user.bp)
# app.register_blueprint(create.bp)
# app.register_blueprint(update.bp)
# app.register_blueprint(read.bp)
# app.register_blueprint(delete.bp)
from app.app import create_app

app=create_app()

if(__name__=='__main__'):
    app.run(debug=True)