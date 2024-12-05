from flask import Flask ,Blueprint,render_template,url_for,redirect

bp=Blueprint('create',__name__)

@bp.route('/create/',methods=['GET','POST'])
def create():
    return render_template('/curd_operation/create.html')