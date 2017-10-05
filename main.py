from flask import request, Flask, redirect
import jinja2
import os
import re

template_dir = os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)

@app.route("/")
def index():
    template = jinja_env.get_template("index.html")
    return template.render(username="",
    password = "",
    v_password = "",
    email = "",
    error_user = False,
    error_password = False,
    error_vpw = False,
    error_email = False)
@app.route("/signup", methods=["POST"])
def signup():
    template = jinja_env.get_template('index.html')
    username = request.form['username']
    password = request.form['password']
    v_password = request.form['password verification']
    email = request.form['email']
    error_user = False
    error_password=False
    error_vpw = False
    error_email = False
    if not username:
        error_user = True
    if (len(password) < 3) or (len(password) > 20) or (len(password) == 0):
        error_pw = True
    if (v_password != password) or (len(v_password) == 0):
        error_vpw = True
    if (len(email) < 3) or (len(email) > 20) and not re.match("[^@]+@[^@]+\.[^@]+", email):
        error_email = True
    if error_user or error_password or error_vpw or error_email:
        return template.render(username="",
    password = "",
    v_password = "",
    email = "",
    error_user = False,
    error_password = False,
    error_vpw = False,
    error_email = False)

    else:
        return redirect("/welcome?username=" + username)
    @app.route("/welcome", methods=["GET"])
    def welcome():
        username = request.args.get("username")
        template = jinja_env.get_template("welcome.html")
        return template.render(username)
    
    app.run(debug=True)
    