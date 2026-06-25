from redis_client import client

try:
    response = client.ping()
    print("Connected to Redis!")
    print("Ping Response:", response)

except Exception as e:
    print("Connection Failed!")
    print(e)