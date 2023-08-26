import json


# Example on how to test flask app
def test_schemes(client):
    response = client.get("/schemes")
    response_data = json.loads(response.data)
    assert response_data == ["random", "simultaneous", "alternative", "single", None]
