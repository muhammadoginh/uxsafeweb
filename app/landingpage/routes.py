from app.landingpage import blueprint
from flask import render_template


@blueprint.route('/')
def landingpage():
    return render_template('landingpage.html')
