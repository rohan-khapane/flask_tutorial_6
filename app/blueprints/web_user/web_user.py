from flask import Flask , Blueprint,render_template,redirect

bp=Blueprint("web_user",__name__)

@bp.route('/web_user/')
def web_user():
    return render_template('web_user/web_user_home.html')