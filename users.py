from db import db
from flask import session
import secrets
from werkzeug.security import check_password_hash, generate_password_hash


def signup(username, password, role_id):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, role_id) VALUES (:username,:password,:role_id)"
        db.session.execute(sql, {"username":username, "password":hash_value, "role_id":role_id})
        db.session.commit()
    except Exception:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]

def login(username, password):
    sql = "SELECT username, id, password, role_id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = user.username
            session["user_id"] = user.id
            session["role_id"] = user.role_id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def is_admin():
    sql = "SELECT U.role_id FROM users U WHERE U.id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id()})
    role_id = result.fetchone()
    secret_key = role_id.role_id
    print(role_id.role_id)
    if secret_key == 2:
        return True
    else:
        return False

def add_reputation(id):
    try:
        sql = "INSERT INTO reputation (user_id) VALUES (:user_id)"
        db.session.execute(sql, {"user_id":id})
        db.session.commit()
    except Exception:
        return False
    return True

def get_reputation():
    print("menee sql")
    sql = "SELECT U.username, COUNT(R.user_id) FROM reputation R, users U WHERE U.id=R.user_id GROUP BY U.username ORDER BY COUNT(R.user_id) DESC"
    result = db.session.execute(sql)
    fetch_reputation = result.fetchall()
    if not fetch_reputation:
        return False
    else:
        return fetch_reputation


