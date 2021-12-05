from db import db
import users

def get_messages(id):
    sql = "SELECT U.username, M.content, M.sent_at, T.id, T.subjects FROM messages M, topics T, users U " \
        "WHERE M.topic_id=T.id AND T.id=:id ORDER BY M.sent_at"
    result = db.session.execute(sql, {"id":id})
    fetch_messages = result.fetchall()
    if not fetch_messages:
        return False
    else:
        return fetch_messages

def new_message(message, visibility, topic_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO messages (topic_id, content, user_id, visibility) VALUES (:topic_id, :content, :user_id, :visibility)"
    db.session.execute(sql, {"topic_id":topic_id, "content":message, "user_id":user_id, "visibility":visibility})
    db.session.commit()
    return True

def search_messages(query):
    sql = "SELECT U.username, T.subjects, M.topic_id, M.id, M.content, M.sent_at FROM messages M, users U, topics T " \
        "WHERE M.topic_id=T.id AND content LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    fetch_messages = result.fetchall()
    if not fetch_messages:
        return False
    else:
        return fetch_messages
