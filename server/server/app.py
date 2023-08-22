from flask import Flask, request
from flask_cors import CORS
from experiments.run import simulate_without_saving
import networkx as nx

app = Flask(__name__)
CORS(app)


@app.route("/simulate", methods=["GET"])
def simulate():
    finish_time = request.json.get("finishTime")
    mtd_interval = request.json.get("mtdInterval")
    scheme = request.json.get("scheme")
    total_nodes = request.json.get("totalNodes")
    if not all([finish_time, mtd_interval, scheme, total_nodes]):
        return {}, 400

    result = simulate_without_saving(
        start_time=0,
        finish_time=finish_time,
        mtd_interval=mtd_interval,
        scheme=scheme,
        total_nodes=total_nodes,
    )

    resulting_graph = nx.node_link_data(result.get_network().graph)
    for node in resulting_graph["nodes"]:
        node["host"] = node["host"].to_json()

    return resulting_graph, 200


@app.route("/health", methods=["GET"])
def health_check():
    return {"health": "OK!"}, 200
