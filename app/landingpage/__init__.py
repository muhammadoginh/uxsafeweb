from flask import Blueprint

blueprint = Blueprint(
    'landing_blueprint',
    __name__,
    template_folder='templates',
    static_folder='static'
)
