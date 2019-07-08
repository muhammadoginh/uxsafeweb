from app.error import blueprint
from flask import render_template
from app import login_manager


# @login_manager.unauthorized_handler
# def unauthorized():
#     return render_template('page_401.html'), 401