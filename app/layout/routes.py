from bcrypt import checkpw
from flask import jsonify, render_template, redirect, request, url_for

from app.layout import blueprint


@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')

@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))

@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

    return 'Server shutting down...'
