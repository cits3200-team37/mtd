# API Endpoints

## `[POST] /simulate`

#### Description

This endpoint runs the `simulate_without_saving` function that can be found in `experiments/run.py`. It returns the resulting evaluation details of the simulation. Some elements such as the MTD Record and Attack Record require restructuring / further processing on the frontend to extract relevant data and be compatible with the Javascript graphing library [d3](https://d3js.org/).

#### Request body

```
{
  "finishTime":int (optional),
  "mtdInterval":int,
  "scheme":string,
  "totalNodes":int,
  "seed": int (optional)
}
```

#### Sample request

```json
{
  "finishTime": 3000,
  "mtdInterval": 200,
  "scheme": "random",
  "totalNodes": 100
}
```

#### Sample response

```json
{
  "network": {},
  "mtd_record": {},
  "attack_record": {},
  "comp_hosts": [],
  "exposed_hosts": [],
  "comp_checkpoint": [],
}
```
All elements are derived from the Evaluation Class using the final network and adversary state once the simulation has terminated.

##### Response Elements
- `network` contains the graph of the network from the _network object. The `host` element of the nodes in the graph have been converted to json for compatibility with the [d3 library](https://d3js.org/).
- `mtd_record`and `attack_record` comprise the records of the total operation of the simulation, what attack and defense methods were utilised, as well as when and where.
- `comp_hosts` is a list of the hosts compromised by the adversary during the simulation.
- `exposed_hosts` is a list of hosts "visible" to potential attackers. It is derived from the network objects nodes and is the set of exposed endpoints, all reachable nodes and their direct neighbours.
- `comp_checkpoint` contains some of the key metrics of the simulation at particular percentages of compromise.

#### Request Parameters

- `finishTime` is an optional parameter, if `finishTime` is not provided, the simulation runs till the network reaches compromised threshold (compromise ratio > 0.9)
    - Stable test limit: `None` or 10 <= `finishTime` <= 5000
- `startTime` is the time to start the simulation
    - Stable test limit: `startTime` >= 0
    - Logical limit: `startTime` <= `finishTime`
- `mtdInterval` is the time imterval ot trigger MTD(s)
    - Stable test limit: `mtdInterval` > 0; no apparent upward limit
    - Logical limit: `mtdInterval` <= `finishTime` - `startTime`
- `scheme` is the mtd scheme to be used, please get available schemes from schemes endpoint TODO
    - Stable test limit: "random" or "simultaneous" or "alternative"; "single" and None produce error
- `totalNodes` is the number of nodes in the network (network size)
    - Stable test limit: 20 <= `totalNodes` <= 1000
- `seed` can be provided to replicate simulations.
- `totalEndpoints` is the number of exposed nodes
    - Stable test limit: `totalEndpoints` > 0 and `totalEndpoints` < `totalNodes`
-  `totalSubnets` is the number of subnets
    - Logical limit: (`totalNodes` - `totalEndpoints`) / (`totalSubnets` - 1) > 2
- `totalLayers` is the number of layers in the network
    - Stable test limit: 0 < `totalLayers` <= 12
    - Input above 12 causes index error as mtdnetwork\network.py loops through constant array of hosts
- `targetLayer` is the target layer in the network
    - No known limit causes error
- `totalDatabase` is the number of database nodes used for computing DAP algorithm
    - No known limit causes error
- `terminateCompromiseRatio` is the compromised ratio at which the simulation will terminate
    - Logical limit: 0.0 < `terminateCompromiseRatio` <= 1.0

