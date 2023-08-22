import json


# Example on how to test flask app
def test_health(client):
    response = client.get("/health")
    response_data = json.loads(response.data)
    assert response_data == {"health": "OK!"}
