from flask import Blueprint,redirect,render_template,url_for,flash,request


auth_bp = Blueprint("auth", __name__, template_folder="templates", static_folder="static",static_url_path="/")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    return "register"


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    return "login"

