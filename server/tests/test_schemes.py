def test_schemes(client):
    response = client.get("/schemes")
    response_data = response.get_json()
    assert response_data == ["random", "simultaneous", "alternative", "single"]
