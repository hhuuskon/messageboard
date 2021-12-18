from os import abort
from app import app
from flask import render_template, request, redirect, session
import users
import topics
import messages
from db import db

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
            return render_template("/login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_verif = request.form["password_verif"]
        role_id = request.form["role_id"]
        if password != password_verif:
            return render_template("error.html", get_back="/signup", message="Salasanat eroavat toisistaan")
        if users.signup(username, password, role_id):
            return redirect("/topics")
        else:
            return render_template("error.html", get_back="/signup", message="Käyttäjätunnuksen tekemisessä meni jotain pieleen.")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("/login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/topics")
        else:
            return render_template("error.html", get_back="/login", message="Tarkista salasana ja tunnus")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/login")

@app.route("/topics")
def get_topics():
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään.")
    if not topics.get_topics():
        return render_template("topics.html", count=0)
    else:
        list = topics.get_topics()
        return render_template("topics.html", count=len(list), topics=list)

@app.route("/newtopic", methods=["GET", "POST"])
def new_topic():
    allow = False
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään.")
    if users.is_admin():
        allow = True
    if not allow:
        return render_template("error.html", get_back="/topics", message="Vain ylläpitäjät pystyvät luomaan uusia aiheita. " \
        "Tarkista, että olet kirjautunut sisään ylläpitäjänä.")
    if request.method == "GET":
        return render_template("/newtopic.html")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        topic = request.form["new_topic"]
        visibility = request.form["visibility"]
        if topics.new_topic(topic, visibility):
            return redirect("/topics")
        else:
            return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")

@app.route("/messages/<int:id>")
def get_messages(id):
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")
    if not messages.get_messages(id):
        return render_template("messages.html", count=0, subject="test", message_id=id)
    else:
        list = messages.get_messages(id)
        subject = list[0][4]
        return render_template("messages.html", count=len(list), messages=list, subject=subject, message_id=id)

@app.route("/newmessage/<int:id>", methods=["GET", "POST"])
def new_message(id):
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")
    if request.method == "GET":
        return render_template("/newmessage.html", message_id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        message = request.form["new_message"]
        visibility = request.form["visibility"]
        if messages.new_message(message, visibility, id):
            return redirect(f"/messages/{id}")
        else:
            return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")

@app.route("/result")
def result():
    query = request.args["query"]
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")
    if not messages.search_messages(query):
        return render_template("error.html", get_back="/topics", message="Tällä hakusanalla ei tuloksia.")
    if len(query) <= 0:
        return render_template("error.html", get_back="/topics", message="Syötä hakusana!")
    else:
        list = messages.search_messages(query)
        return render_template("result.html", count=len(list), messages=list)

@app.route("/submessages/<int:id>")
def get_submessages(id):
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")
    if not messages.get_submessages(id):
        return render_template("submessages.html", count=0, subject="", message_id=id)
    else:
        list = messages.get_submessages(id)
        subject = list[0][4]
        m_id = list[0][3]
        return render_template("submessages.html", count=len(list), messages=list, subject=subject, message_id=id, m_id=m_id)

@app.route("/newsubmessage/<int:id>", methods=["GET", "POST"])
def new_submessage(id):
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")
    if request.method == "GET":
        return render_template("/newsubmessage.html", message_id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        message = request.form["new_submessage"]
        visibility = 0
        if messages.new_submessage(message, visibility, id):
            return redirect(f"/submessages/{id}")
        else:
            return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")

@app.route("/ownmessages")
def search_own_messages():
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")
    if not messages.search_own_messages(user_id):
        return render_template("error.html", get_back="/topics", message="Et ole tainnut kirjottaa viestejä.")
    else:
        list = messages.search_own_messages(user_id)
        return render_template("ownmessages.html", count=len(list), messages=list)


@app.route("/modifymessage/<int:id>", methods=["GET", "POST"])
def modifymessage(id):
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")
    if request.method == "GET":
        message = messages.get_message_to_modify(id, user_id)
        return render_template("/modifymessage.html", message=message, message_id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        message = request.form["modifymessage"]
        if messages.modifymessage(message, id):
            return redirect("/ownmessages")
        else:
            return render_template("error.html", get_back="/login", message="Tarkista, että olet kirjautunut sisään")