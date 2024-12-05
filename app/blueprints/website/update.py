from flask import Flask,Blueprint,render_template,url_for

bp=Blueprint('update',__name__)

@bp.route('/update/',methods=['GET','PUT'])
def update():
    return render_template('/curd_operation/update.html')