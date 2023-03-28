from app.auth import bp
from flask import render_template
from .forms import LoginForm, RegistrationForm

@bp.route("/")
@bp.route("/index/")
def index():
    return render_template("index.html")

@bp.route("/login/")
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)

@bp.route("/register/")
def register():
    regis_form = RegistrationForm()
    return render_template("auth/register.html", form=regis_form)



