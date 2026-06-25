from session_manager import create_session
from pprint import pprint
session = create_session(
    {
        "name": "Manjula",
        "email": "manjumallepeddi@gmail.com"
    }
)

pprint(session)