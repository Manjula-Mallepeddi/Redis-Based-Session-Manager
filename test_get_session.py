from session_manager import create_session
from session_manager import get_session


session = create_session(
    {
        "name": "Manjula",
        "email": "manjumallepeddi@gmail.com"
    }
)

session_id = session["session_id"]

print("Created Session:")
print(session)

print("\nRetrieved Session:")
print(get_session(session_id))