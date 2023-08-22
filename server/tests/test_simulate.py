import json


def assert_response_equals_expected(response, expected):
    assert response["directed"] == expected["directed"]
    assert response["graph"] == expected["graph"]
    assert response["multigraph"] == expected["multigraph"]

    # check links match
    assert len(response["links"]) == len(expected["links"])
    for link in response["links"]:
        assert link in expected["links"]

    assert len(response["nodes"]) == len(expected["nodes"])

    for node in response["nodes"]:
        del node["host"]["hostUuid"]

    for node in expected["nodes"]:
        del node["host"]["hostUuid"]

    for node in response["nodes"]:
        assert node in expected["nodes"]


def test_mtd_simulation_none(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "scheme": "None",
        "totalNodes": 50,
        "seed": 3200,
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 200

    response_data = json.loads(response.data)
    expected_response = None

    with open("./tests/data/mtd_simulation_none.json", "r") as f:
        expected_response = json.load(f)

    assert_response_equals_expected(response_data, expected_response)
