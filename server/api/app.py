from flask import Flask, request
from flask_cors import CORS
from experiments.run import simulate_without_saving
from mtdnetwork.mtd.completetopologyshuffle import CompleteTopologyShuffle
from mtdnetwork.mtd.ipshuffle import IPShuffle
from mtdnetwork.mtd.osdiversity import OSDiversity
from mtdnetwork.mtd.servicediversity import ServiceDiversity
import networkx as nx

app = Flask(__name__)
CORS(app)


strategy_mapping = {
    "IP Shuffle": IPShuffle,
    "OS Diversity": OSDiversity,
    "Service Diversity": ServiceDiversity,
    "Complete Topology Shuffle": CompleteTopologyShuffle,
}


@app.route("/strategies", methods=["GET"])
def strategies():
    # Provides the currently availble strategies

    # NOTE: this is so that strategies can be added in future
    # update strategy_mapping to add strategy
    return list(strategy_mapping.keys()), 200


@app.route("/simulate", methods=["POST"])
def simulate():
    finish_time = request.json.get("finishTime")
    mtd_interval = request.json.get("mtdInterval")
    scheme = request.json.get("scheme")
    total_nodes = request.json.get("totalNodes")
    seed = request.json.get("seed")
    total_layers = request.json.get("totalLayers")
    total_endpoints = request.json.get("totalEndpoints")
    total_subnets = request.json.get("totalSubnets")
    total_layers = request.json.get("totalLayers")
    target_layer = request.json.get("targetLayer")
    total_database = request.json.get("totalDatabase")
    terminate_compromise_ratio = request.json.get("terminateCompromiseRatio")
    strategies = request.json.get("strategies")

    custom_strategies = None

    if not all([mtd_interval, scheme, total_nodes]):
        return {}, 400

    # NOTE: custom strategies are ignored if scheme is in random or None
    if scheme is not None and scheme not in ["random", "None"]:
        if strategies is None:
            return {"error": "MTD strategy not specified"}, 400
        custom_strategies = []
        for strategy in strategies:
            if strategy not in strategy_mapping.keys():
                return {"error": f"Strategy '{strategy}' does not exist"}, 400
            custom_strategies.append(strategy_mapping.get(strategy))

    if scheme == "single" and len(custom_strategies) > 1:
        return {"error": "More than one MTD strategy specified for single scheme"}, 400

    result = simulate_without_saving(
        finish_time=finish_time,
        mtd_interval=mtd_interval,
        scheme=scheme,
        total_nodes=total_nodes,
        seed=seed,
        total_endpoints=total_endpoints,
        total_subnets=total_subnets,
        total_layers=total_layers,
        target_layer=target_layer,
        total_database=total_database,
        terminate_compromise_ratio=terminate_compromise_ratio,
        custom_strategies=custom_strategies,
    )

    data = {}
    net_graph = nx.node_link_data(result._network.graph)
    for node in net_graph["nodes"]:
        node["host"] = node["host"].to_json()

    data["network"] = net_graph
    data["mtd_record"] = result._mtd_record.to_dict()
    data["attack_record"] = result._attack_record.to_dict()
    data["comp_hosts"] = result._adversary.get_compromised_hosts()

    visible_hosts = set()
    for c_host in result._network.reachable:
        visible_hosts.update(set(result._network.graph.neighbors(c_host)))

    visible_hosts.update(result._network.reachable)
    visible_hosts.update(result._network.exposed_endpoints)

    data["exposed_hosts"] = list(visible_hosts)

    data["comp_checkpoint"] = result.evaluation_result_by_compromise_checkpoint()

    return data, 200


@app.route("/schemes", methods=["GET"])
def schemes():
    return ["random", "simultaneous", "alternative", "single", "None"], 200


@app.route("/health", methods=["GET"])
def health_check():
    return {"health": "OK!"}, 200
