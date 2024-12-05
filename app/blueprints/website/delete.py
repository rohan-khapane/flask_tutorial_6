from flask import Flask ,Blueprint,render_template,url_for

bp=Blueprint('delete',__name__)

@bp.route('/delete/',methods=['GET','DELETE'])
def delete():
    return render_template('/curd_operation/delete.html')