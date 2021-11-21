from db import db
import users

def get_topics():
    sql = "SELECT T.subjects, U.username, T.sent_at FROM topics T, users U " \
        "WHERE T.user_id=U.id ORDER BY T.sent_at"
    result = db.session.execute(sql)
    fetch_topics = result.fetchall()
    if not fetch_topics:
        return False
    else:
        return fetch_topics

def new_topic(topic, visibility):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO topics (subjects, user_id, visibility) VALUES (:subjects, :user_id, :visibility)"
    db.session.execute(sql, {"subjects":topic, "user_id":user_id, "visibility":visibility})
    db.session.commit()
    return True
