import json
from session_manager import create_session, get_session, update_session

session = create_session(
    {
        "name": "Manjula",
        "email": "manjumallepeddi@gmail.com"
    }
)

print("\nCreated Session:")
print(json.dumps(session, indent=4))

session_id = session["session_id"]

retrieved = get_session(session_id)

print("\nRetrieved Session:")
print(json.dumps(retrieved, indent=4))

updated = update_session(
    session_id,
    {
        "role": "Intern",
        "department": "AI"
    }
)

print("\nUpdated Session:")
print(json.dumps(updated, indent=4))