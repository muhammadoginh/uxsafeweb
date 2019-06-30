from app.home import blueprint
from flask import render_template
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)


@blueprint.route('/home')
@login_required
def home():
    return render_template('index.html')