"""

AUTOR: Israel Bazan

FECHA DE CREACIÓN: 2/09/21

"""

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from werkzeug.urls import url_parse

from forms import TablasForm
from models import users, get_user, User

# from flask_bootstrap import Bootstrap
#from user_agents import parse
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
#Bootstrap(app)


posts = []


# @app.route("/")
# def index():
#     return render_template("index.html", posts=posts)
@app.route("/mock/<string:version>/")
def mock(version):
    return render_template("show_tablas_mock_" + version + ".html", posts=posts)
@app.route("/useragent/")
def func_user_agent():
    ua_string = request.user_agent.string
    #user_agent = parse(ua_string)
    #strIsMobile = "is mobile: " + str(user_agent.is_mobile)
    #return strIsMobile
    return ua_string

# @app.route("/p/<string:slug>/")
# def show_post(slug):
#     return render_template("post_view.html", slug_title=slug)
@app.route("/",methods=['GET','POST'],defaults={'num': 1,'start':1})
@app.route("/<int:num>/<int:start>/",methods=['GET','POST'])
def show_tablas(num,start):
    cols=5
    form = TablasForm()
    if form.validate_on_submit():
        num = form.number.data
    user_agent = parse(request.user_agent.string)
    if user_agent.is_mobile:
        cols = 1
        return render_template("mobile/show_tablas_v1.html", num=num,cols=cols,start=start,form=form)
    else:
        return render_template("show_tablas_v1.html", num=num,cols=cols,start=start,form=form)


       
    