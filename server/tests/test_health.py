# Example on how to test flask app
def test_health(client):
    response = client.get("/health")
    response_data = response.get_json()
    assert response_data == {"health": "OK!"}
