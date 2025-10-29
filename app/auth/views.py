from flask import Blueprint,redirect,render_template,url_for,flash,request,jsonify


auth_bp = Blueprint("auth", __name__, template_folder="templates", static_folder="static",static_url_path="/")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('auth/register.html')
    else:
        data = request.get_json()
        print("registered: ",data)
        return jsonify({"message":"registered"}),201
        
    


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    else: 
        data = request.get_json()
        print("logged in: ",data)

        # check if data submitted is valid
        return jsonify({"message":"logged in"}),200

