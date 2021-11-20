from db import db
import users

def get_topics():
    sql = "SELECT T.subjects, U.username, T.sent_at FROM topics T, users U" \
        "WHERE T.user_id=U.id ORDER BY T.sent_at"
    result = db.session.execute(sql)
    return result.fetchall()

def new_topic(topic):
    user_id = users.user.id()
    visibilitiy = users.user.role_id
    #for test use only
    #user_id = 1
    #visibility = 1
    #username = users.user.username()
    if user_id == 0:
        return False
    sql = "INSERT INTO topics (subjects, user_id, visibility) VALUES (:subjects, :user_id, :visibility)"
    db.session.execute(sql, {"subjects":topic, "user_id":user_id, "visibility":visibility})
    db.session.commit()
    return True
