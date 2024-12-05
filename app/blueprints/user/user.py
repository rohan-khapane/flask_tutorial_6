from flask import Flask , Blueprint,render_template,url_for,redirect

bp=Blueprint("user",__name__)

@bp.route('/')
def index():
    return render_template('curd_operation/create.html')

@bp.route('/user/')
def user():
    return render_template('user/user_home.html')