from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Index page.
    :return: The response.
    """

    return render_template('main/index.html')
