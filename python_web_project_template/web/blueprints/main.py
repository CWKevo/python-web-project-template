from flask import Blueprint, render_template


MAIN_BLUEPRINT = Blueprint('main', __name__)



@MAIN_BLUEPRINT.route('/')
def index():
    return render_template('main/index.html')
