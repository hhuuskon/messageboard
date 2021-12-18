from db import db
import users

def get_messages(id):
    sql = "SELECT DISTINCT U.username, M.content, M.sent_at, T.id, T.subjects, M.id FROM messages M, topics T, users U " \
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
    sql = "SELECT U.username, T.subjects, M.topic_id, M.id, M.content, M.sent_at, S.content FROM messages M, users U, topics T, submessages S " \
        "WHERE M.topic_id=T.id AND S.content LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    fetch_messages = result.fetchall()
    if not fetch_messages:
        return False
    else:
        return fetch_messages

def get_submessages(id):
    sql = "SELECT DISTINCT U.username, S.content, S.sent_at, S.message_id, M.content FROM messages M, users U, submessages S " \
        "WHERE S.message_id=M.id AND M.id=:id ORDER BY S.sent_at"
    result = db.session.execute(sql, {"id":id})
    fetch_messages = result.fetchall()
    if not fetch_messages:
        return False
    else:
        return fetch_messages

def new_submessage(message, visibility, message_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO submessages (message_id, content, visibility) VALUES (:message_id, :content, :visibility)"
    db.session.execute(sql, {"message_id":message_id, "content":message, "visibility":visibility})
    db.session.commit()
    return True

def search_own_messages(user_id):
    sql = "SELECT U.username, M.content, S.message_id, S.content, S.sent_at, S.id FROM messages M, users U, submessages S " \
        "WHERE S.message_id=M.id AND U.id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    fetch_messages = result.fetchall()
    if not fetch_messages:
        return False
    else:
        return fetch_messages

def get_message_to_modify(id, user_id):
    sql = "SELECT S.content, S.message_id FROM messages M, submessages S, users U " \
        "WHERE S.id=:id AND U.id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id, "id":id})
    fetch_messages = result.fetchall()
    if not fetch_messages:
        return False
    else:
        return fetch_messages

def modifymessage(message, message_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "UPDATE submessages SET content=:content WHERE id=:message_id"
    db.session.execute(sql, {"message_id":message_id, "content":message})
    db.session.commit()
    return True
