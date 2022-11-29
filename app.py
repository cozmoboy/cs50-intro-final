import os
#import math
#import ast
import helpers
import classes
import dataBG
import bestiaryAll

# export FLASK_APP=app.py
# export FLASK_DEBUG=1

from cs50 import SQL
# import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import dictionaryWithNameFromArray, makePCofClass

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    # disables caching of responses
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# -----------------  INDEX   ---------------------------
@app.route("/", methods=["GET", "POST"])
# @login_required
def index():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return render_template("/index.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/index.html")


# -----------------  pcMAIN   ---------------------------
@app.route("/pcMain", methods=["GET", "POST"])
def pcMain():
    print('IN pcMAIN ..........', flush=True)
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        cClass = request.form.get("class")
        genre = request.form.get("genre")

        print("Genre: " + genre, flush=True)
        print("Class: " + cClass, flush=True)

        print('inside pcMain POST', flush=True)
        if session.get("pc"):
            # pc = session.get("pc")
            print('EXISTING pc', flush=True)
            # print(pc, flush=True)
            # return render_template("/pcMain.html", pc = pc)

            pc = session.get("pc"):
            return render_template("/pcMain.html", pc=pc)

        else:
            # pc = classes.PC()
            # helpers.savePC(pc);
            print('NEW pc', flush=True)
            # print(pc, flush=True)
            # return render_template("/pcMain.html", pc = pc)

            pc = makePCofClass("Fighter", "fantasy")
            return render_template("/pcMain.html", pc=pc)

    # if session.get("pc"):
    #     pc = session.get("pc")
    # else:
    #     pc = classes.PC()
    print('inside pcMain GET', flush=True)
    return render_template("/pcMain.html")


# -----------------  LOGOUT   ---------------------------
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# -----------------  gmMAIN  ---------------------------
@app.route("/gmMain", methods=["GET", "POST"])
def gmMain():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return render_template("/gmMain.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/gmMain.html")


# -----------------  makePC  views ---------------------------
@app.route("/makePC", methods=["GET", "POST"])
def makePC():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return render_template("/makePC.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/makePC.html")


@app.route("/fantasyPC", methods=["GET", "POST"])
def fantasyPC():
    if request.method == "POST":
        return render_template("/fantasyPC.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:

        return render_template("/fantasyPC.html", genre=dictionaryWithNameFromArray("fantasy", dataBG.GENRES))


@app.route("/westernPC", methods=["GET", "POST"])
def westernPC():
    if request.method == "POST":
        return render_template("/westernPC.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/westernPC.html")


@app.route("/scifiPC", methods=["GET", "POST"])
def scifiPC():
    if request.method == "POST":
        return render_template("/scifiPC.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/scifiPC.html")


@app.route("/postApPC", methods=["GET", "POST"])
def postApPC():
    if request.method == "POST":
        return render_template("/postApPC.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/postApPC.html")


@app.route("/bestiary", methods=["GET", "POST"])
def besiary():
    if request.method == "POST":
        myBestiary = bestiaryAll.BESTIARY
        return render_template("/bestiary.html", bestiary=myBestiary)

    else:
        myBestiary = bestiaryAll.BESTIARY
        return render_template("/bestiary.html", bestiary=myBestiary)
    
@app.route("/updateHP", ethods=["GET", "POST"])
def updateHP():
    
