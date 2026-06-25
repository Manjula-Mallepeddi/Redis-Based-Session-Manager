import json
import uuid
from datetime import datetime

from redis_client import client
from config import SESSION_EXPIRY

def create_session(user_data):
    """
    Creates a new session and stores it in Redis.
    """
     
    session_id = str(uuid.uuid4())
    session = {
        "session_id": session_id,
        "user_data": user_data,
        "last_accessed": datetime.utcnow().isoformat()###
    }

    client.setex(
    session_id,
    SESSION_EXPIRY,
    json.dumps(session)
)

    return session

from datetime import datetime


def get_session(session_id):
    """
    Creates a new session and stores it in Redis.
    """

    data = client.get(session_id)

    if not data:
        return {"error": "Session not found"}

    session = json.loads(data)

    session["last_accessed"] = datetime.utcnow().isoformat()

    client.setex(
    session_id,
    SESSION_EXPIRY,
    json.dumps(session)
)

    return session

def update_session(session_id, new_user_data):
    """
    Creates a new session and stores it in Redis.
    """
    
    data = client.get(session_id)

    if not data:
        return {"error": "Session not found"}

    session = json.loads(data)

    session["user_data"].update(new_user_data)

    session["last_accessed"] = datetime.utcnow().isoformat()

    client.setex(
    session_id,
    SESSION_EXPIRY,
    json.dumps(session)
)

    return session

