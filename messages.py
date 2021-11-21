from db import db
import users

def get_messages():
    sql = "SELECT content, sent_at FROM messages ORDER BY sent_at"
    result = db.session.execute(sql)
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
