from flask import Blueprint,redirect,render_template,url_for,flash,request


dash_bp = Blueprint("dash", __name__, template_folder="templates", static_folder="static",static_url_path="/")


@dash_bp.route("/", methods=["GET", "POST"])
def dashboard():
    return "dash"