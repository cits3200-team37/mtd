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

    # for node in response["network"]["nodes"]:
    #     assert node in expected["network"]["nodes"]


def test_mtd_simulation_none(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "totalNodes": 50,
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 200

    response_data = response.get_json()
    expected_response = None

    with open("./tests/data/mtd_simulation_none.json", "r") as f:
        expected_response = json.load(f)

    assert_response_equals_expected(response_data, expected_response)


def test_mtd_simulation_random(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "scheme": "random",
        "totalNodes": 50,
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 200

    response_data = response.get_json()
    expected_response = None

    with open("./tests/data/mtd_simulation_random.json", "r") as f:
        expected_response = json.load(f)

    assert_response_equals_expected(response_data, expected_response)


def test_mtd_simulation_single(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "scheme": "single",
        "totalNodes": 50,
    }
    strategies = [
        "IP Shuffle",
        "OS Diversity",
        "Service Diversity",
        "Complete Topology Shuffle",
    ]
    for strategy in strategies:
        req_body["strategies"] = [strategy]

        response = client.post("/simulate", json=req_body)
        assert response.status_code == 200

        response_data = response.get_json()
        expected_response = None

        with open(
            f"./tests/data/mtd_simulation_single_{strategy.replace(' ','_')}.json", "r"
        ) as f:
            expected_response = json.load(f)

        assert_response_equals_expected(response_data, expected_response)


def test_mtd_simulation_alternative(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "scheme": "alternative",
        "totalNodes": 50,
        "strategies": ["IP Shuffle", "OS Diversity"],
    }

    response = client.post("/simulate", json=req_body)
    assert response.status_code == 200

    response_data = response.get_json()
    expected_response = None

    with open("./tests/data/mtd_simulation_alternative.json", "r") as f:
        expected_response = json.load(f)

    assert_response_equals_expected(response_data, expected_response)


def test_mtd_simulation_simulatneous(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "scheme": "simultaneous",
        "totalNodes": 50,
        "strategies": [
            "IP Shuffle",
            "OS Diversity",
            "Service Diversity",
            "Complete Topology Shuffle",
        ],
    }

    response = client.post("/simulate", json=req_body)
    assert response.status_code == 200

    response_data = response.get_json()
    expected_response = None

    with open("./tests/data/mtd_simulation_simultaneous.json", "r") as f:
        expected_response = json.load(f)

    assert_response_equals_expected(response_data, expected_response)


def test_scheme_does_not_exist(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "totalNodes": 50,
        "scheme": "CITS3200",
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 400
    assert response.get_json() == {"error": "scheme CITS3200 does not exist"}


def test_multiple_strategies_for_single_scheme(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "totalNodes": 50,
        "scheme": "single",
        "strategies": [
            "IP Shuffle",
            "OS Diversity",
            "Service Diversity",
            "Complete Topology Shuffle",
        ],
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 400
    assert response.get_json() == {
        "error": "More than one MTD strategy specified for single scheme"
    }


def test_strategy_does_not_exist(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "totalNodes": 50,
        "scheme": "single",
        "strategies": [
            "IP Shuffle",
            "CITS3200",
            "Service Diversity",
            "Complete Topology Shuffle",
        ],
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 400
    assert response.get_json() == {"error": "Strategy 'CITS3200' does not exist"}


def test_strategy_not_specified(client):
    req_body = {
        "finishTime": 3000,
        "mtdInterval": 200,
        "totalNodes": 50,
        "scheme": "single",
    }
    response = client.post("/simulate", json=req_body)
    assert response.status_code == 400
    assert response.get_json() == {"error": "MTD strategy not specified"}
