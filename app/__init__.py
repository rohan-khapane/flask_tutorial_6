from flask import Flask
from app.blueprints.user import user
from app.blueprints.web_user import web_user


app=Flask(__name__)
#app.secret_key
app.register_blueprint(user.bp)
app.register_blueprint(web_user.bp)


if(__name__=='__main__'):
    app.run(debug=True)