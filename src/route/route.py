from flask import (
    Blueprint
)
bp = Blueprint('route', __name__)


@bp.route('/')
def index():
    return 'Routes...'
