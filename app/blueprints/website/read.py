from flask import Flask ,Blueprint,render_template,url_for,redirect

bp=Blueprint('read',__name__)

@bp.route('/read/',methods=['GET'])
def read():
    return render_template('/curd_operation/read.html')