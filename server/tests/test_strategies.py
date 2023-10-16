def test_schemes(client):
    response = client.get("/strategies")
    response_data = response.get_json()
    assert response_data == [
        "IP Shuffle",
        "OS Diversity",
        "Service Diversity",
        "Complete Topology Shuffle",
    ]
