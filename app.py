import classes
import dataBG
import bestiaryAll

# export FLASK_APP=app.py
# export FLASK_DEBUG=1

from cs50 import SQL
# import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import dictionaryWithNameFromArray, makePCofClass, setCurrentHP
from operator import itemgetter

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
        
        pc = makePCofClass(cClass, genre)
        return render_template("/pcMain.html", pc=pc)

    if session.get("pc"):
        print('EXISTING pc', flush=True)
        pc = session.get("pc")
        return render_template("/pcMain.html", pc=pc)
    
    return render_template("/pcMain.html", pc=pc)


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


@app.route("/bestiary", methods=["GET", "POST"])
def besiary():
    if request.method == "POST":
        myBestiary = bestiaryAll.BESTIARY
        newlist = sorted(myBestiary, key=lambda d: d['name'])
        return render_template("/bestiary.html", bestiary=newlist)

    else:
        myBestiary = bestiaryAll.BESTIARY
        newlist = sorted(myBestiary, key=lambda d: d['name'])
        return render_template("/bestiary.html", bestiary=newlist)
    
    
@app.route("/updateHP", methods=["GET", "POST"])
def updateHP():
    
    newHP = request.form.get("currentHPInput")
    setCurrentHP(newHP)

    return redirect("/pcMain.html")
    
    
@app.route("/rules", methods=["GET", "POST"])
def rules():
    if request.method == "POST":
        return render_template("/rules.html")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/rules.html")
    
@app.route("/battleGM", methods=["GET", "POST"])
def battleGM():
    if request.method == "POST":

        enemies = request.form.getlist('name')
        numbers = request.form.getlist('quantity')
        
        allFoes = []
        i = 0
        while i<len(enemies):
            
            if numbers[i] != '':
            
                myDict = {
                    "enemy": dictionaryWithNameFromArray(enemies[i], bestiaryAll.BESTIARY),
                    "number": int(numbers[i])
                }
                allFoes.append(myDict)
                
            i += 1
        
        return render_template("/battleGM.html", allFoes = allFoes)
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        print("You got there by GET <<<<<<<<<<<<<<<", flush=True)
        return redirect("/bestiary.html")