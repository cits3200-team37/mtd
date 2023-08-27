from flask import Flask, request
from flask_cors import CORS
from experiments.run import simulate_without_saving
import networkx as nx
import json

app = Flask(__name__)
CORS(app)


@app.route("/simulate", methods=["POST"])
def simulate():
    finish_time = request.json.get("finishTime")
    mtd_interval = request.json.get("mtdInterval")
    scheme = request.json.get("scheme")
    total_nodes = request.json.get("totalNodes")
    seed = request.json.get("seed")

    if not all([finish_time, mtd_interval, scheme, total_nodes]):
        return {}, 400

    result = simulate_without_saving(
        start_time=0,
        finish_time=finish_time,
        mtd_interval=mtd_interval,
        scheme=scheme,
        total_nodes=total_nodes,
        seed=seed,
    )

    data = {}

    

    net_graph = nx.node_link_data(result._network.graph)
    for node in net_graph["nodes"]:
            node["host"] = node["host"].to_json()
    data["network"] = net_graph

    data["mtd_record"] = result._mtd_record.to_json()
    data["attack_record"] = result._attack_record.to_json()
    
    ## redundant but easier to access, all in network ##

    # data["hosts"] = result._network.get_hosts()
    # data["unique_subnets"] = result._network.get_unique_subnets()
    # data["subnets"] = result._network.get_subnets()
    # data["layers"] = result._network.get_layers()

    data["comp_hosts"] = result._adversary.get_compromised_hosts()

    visible_hosts = []
    for c_host in result._network.reachable:
        visible_hosts = visible_hosts + list(result._network.graph.neighbors(c_host))

    visible_hosts = visible_hosts + result._network.reachable
    visible_hosts = visible_hosts + result._network.exposed_endpoints
        
    data["exposed_hosts"] = visible_hosts

    data["comp_checkpoint"] = result.evaluation_result_by_compromise_checkpoint()

    return json.dumps(data), 200, {'Content-Type': 'application/json'}


@app.route("/health", methods=["GET"])
def health_check():
    return {"health": "OK!"}, 200
