from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


def signup(username, password, role_id):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, role_id) VALUES (:username,:password,:role_id)"
        db.session.execute(sql, {"username":username, "password":hash_value, "role_id":role_id})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]

def login(username, password):
    sql = "SELECT username, id, password FROM users WHERE username=username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = user.username
            session["user_id"] = user.id
            return True
        else:
            return False