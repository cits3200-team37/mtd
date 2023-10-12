import json


def assert_response_equals_expected(response, expected):
    assert response["network"]["directed"] == expected["network"]["directed"]
    assert response["network"]["graph"] == expected["network"]["graph"]
    assert response["network"]["multigraph"] == expected["network"]["multigraph"]

    # check links match
    assert len(response["network"]["links"]) == len(expected["network"]["links"])
    for link in response["network"]["links"]:
        assert link in expected["network"]["links"]

    assert len(response["network"]["nodes"]) == len(expected["network"]["nodes"])

    for node in response["network"]["nodes"]:
        del node["host"]["hostUuid"]

    for node in expected["network"]["nodes"]:
        del node["host"]["hostUuid"]

    for node in response["network"]["nodes"]:
        assert node in expected["network"]["nodes"]


def test_mtd_simulation_none(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "scheme": "random",
        "totalNodes": 50,
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 200

    response_data = json.loads(response.data)
    expected_response = None

    with open("./tests/data/mtd_simulation_random.json", "r") as f:
        expected_response = json.load(f)

    assert_response_equals_expected(response_data, expected_response)
