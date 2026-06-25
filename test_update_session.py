from session_manager import create_session
from session_manager import update_session

session = create_session(
    {
        "name": "Manjula",
        "email": "manjumallepeddi@gmail.com"
    }
)

session_id = session["session_id"]

updated_session = update_session(
    session_id,
    {
        "role": "Intern",
        "department": "AI"
    }
)

print(updated_session)