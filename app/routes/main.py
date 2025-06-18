from flask import Blueprint, render_template
from app.models import get_sql_server_version

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template("index.html")

@main_bp.route('/version')
def version():
    try:
        version_string = get_sql_server_version()
        return render_template("version.html", version=version_string)
    except Exception as e:
        return render_template("version.html", version="Error: " + str(e)), 500

@main_bp.errorhandler(500)
def internal_error(e):
    return "Placeholder for now, should be a dedicated page. 500", 500

@main_bp.errorhandler(404)
def internal_error(e):
    return "Placeholder for now, should be a dedicated page. 404", 500

