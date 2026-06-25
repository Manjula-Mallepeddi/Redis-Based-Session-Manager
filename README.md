# Redis-Backed Session Manager

## Overview

The Redis-Backed Session Manager is a Python utility that manages user sessions using Redis as the storage backend.

The application supports creating, retrieving, and updating session data while maintaining fast access times through Redis. Sessions are automatically expired using Redis TTL (Time To Live) functionality, improving both security and resource management.

## Objective

Build a fast and secure session management system that stores session information as JSON objects in Redis.

## Features

* Create user sessions with unique session IDs
* Store session data in Redis
* Retrieve existing sessions
* Update session information
* Track last accessed timestamps
* Automatic session expiration using Redis TTL
* Error handling for invalid or missing sessions

## Project Structure

```text
redis_session_manager/
 .gitignore
 config.py
 main.py
 README.md
 redis_client.py
 requirements.txt
 session_manager.py
 test_connection.py
 test_get_session.py
 test_session.py
 test_update_session.py
```

## Technologies Used

* Python 3
* Redis
* redis-py (Python Redis Client)
* WSL Ubuntu (Windows Subsystem for Linux)

## Session Format

Example session object:

```json
{
  "session_id": "xyz123",
  "user_data": {
    "name": "Manjula",
    "email": "user@example.com"
  },
  "last_accessed": "2026-06-24T15:00:00"
}
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd redis_session_manager
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Redis Server

```bash
redis-server
```

## Usage

Run the application:

```bash
python main.py
```

The program will:

1. Create a session
2. Retrieve the session
3. Update session data
4. Display the results

## Example Output

```python
Created Session:
{
    'session_id': 'abc123',
    'user_data': {
        'name': 'Manjula',
        'email': 'manjumallepeddi@gmail.com'
    },
    'last_accessed': '2026-06-24T15:00:00'
}

Retrieved Session:
{
    "session_id": "91e5bb85-5fb6-4be1-baaf-462a31081b99",
    "user_data": {
        "name": "Manjula",
        "email": "manjumallepeddi@gmail.com"
    },
    "last_accessed": "2026-06-24T15:31:28.447002"
}

Updated Session:
{
    'user_data': {
        'name': 'Manjula',
        'email': 'manjumallepeddi@gmail.com',
        'role': 'Intern',
        'department': 'AI'
    }
}
```

## Key Concepts

### Session Creation

Generates a unique session ID and stores session data in Redis.

### Session Retrieval

Fetches session data and updates the last accessed timestamp.

### Session Update

Modifies existing session information and refreshes the session expiration timer.

### Session Expiration (TTL)

Redis automatically removes inactive sessions after the configured expiration period.

## Future Improvements

* Delete session functionality
* User authentication integration
* Session validation middleware
* REST API integration using Flask or FastAPI
* Session analytics and monitoring

## Author

Manjula Mallepeddi
