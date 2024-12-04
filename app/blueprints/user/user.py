from flask import Flask , Blueprint,render_template,url_for,redirect

bp=Blueprint("user",__name__)

@bp.route('/user/')
def user():
    return render_template('user/user_home.html')