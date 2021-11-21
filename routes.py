from app import app
from flask import render_template, request, redirect, session
import users
import topics
import messages

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
            return render_template("error.html", message="Salasanat eroavat toisistaan")
        if users.signup(username, password, role_id):
            return redirect("/topics")
        else:
            return render_template("error.html", message="Käyttäjätunnuksen tekemisessä meni jotain pieleen.")


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
            return render_template("error.html", message="Tarkista salasana ja tunnus")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/login")

@app.route("/topics")
def get_topics():
    if not topics.get_topics():
        return render_template("topics.html", count=0)
    else:
        list = topics.get_topics()
        return render_template("topics.html", count=len(list), topics=list)

@app.route("/newtopic", methods=["GET", "POST"])
def new_topic():
    if request.method == "GET":
        return render_template("/newtopic.html")
    if request.method == "POST":
        topic = request.form["new_topic"]
        visibility = request.form["visibility"]
        if topics.new_topic(topic, visibility):
            return redirect("/topics")
        else:
            return render_template("error.html", message="Tarkista, että olet kirjautunut sisään admin oikeuksilla")

@app.route("/messages")
def get_messages():
    if not messages.get_messages():
        return render_template("messages.html", count=0)
    else:
        list = messages.get_messages()
        return render_template("messages.html", count=len(list), messages=list)

@app.route("/newmessage", methods=["GET", "POST"])
def new_message():
    if request.method == "GET":
        return render_template("/newmessage.html")
    if request.method == "POST":
        message = request.form["new_message"]
        visibility = request.form["visibility"]
        topic_id = request.form["topic_id"]
        if messages.new_message(message, visibility, topic_id):
            return redirect("/messages")
        else:
            return render_template("error.html", message="Tarkista, että olet kirjautunut sisään admin oikeuksilla")
