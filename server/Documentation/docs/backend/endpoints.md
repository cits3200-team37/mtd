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
- Main
```json
{
  "network": {},
  "mtd_record": {},
  "attack_record": {},
  "compromise_checkpoint_metrics": [],
}
```
- network
```json
{
  "network": {
    "directed": false,
    "links": [
      { "source": 0, "target": 13 },
      { "source": 2, "target": 10 },
      ...
    ],
    "nodes": [
      {
        "host": {
          "compromised": true,
          "compromisedServices": [1, 3, 4, 6, 7, 9],
          "hostId": 0,
          "hostUuid": "4806a31a-3f71-4a8d-99d8-880f83547621",
          "ip": "161.99.9.59",
          "osType": "freebsd",
          "osVersion": "12",
          "pUCompromise": false,
          "totalNodes": 10,
          "totalServices": 9,
          "totalUsers": 5
        },
        "id": 0,
        "layer": 0,
        "subnet": 0
      },
      {
        "host": {
          "compromised": false,
          "compromisedServices": [],
          "hostId": 1,
          "hostUuid": "321663a6-13f5-4b2e-bb94-109b4a7b3899",
          "ip": "169.179.214.27",
          "osType": "centos",
          "osVersion": "8",
          "pUCompromise": false,
          "totalNodes": 8,
          "totalServices": 7,
          "totalUsers": 5
        },
        "id": 1,
        "layer": 0,
        "subnet": 0
      },
      ...
    ]
  }
}
```
- MTD Record
```json
{
'name': {0: 'CompleteTopologyShuffle', 1: 'OSDiversity', 2: 'OSDiversity'},
'start_time': {0: 0.0, 1: 200.3685748174762, 2: 400.9527232348661},
'finish_time': {0: 121.81486938465021, 1: 280.6090999799783, 2: 481.0931564591807},
'duration': {0: 121.81486938465021, 1: 80.24052516250208, 2: 80.14043322431462},
'executed_at': {0: 'network', 1: 'application', 2: 'application'}
}
```
- Attack Record
```json
{
'name': {0: 'SCAN_HOST', 1: 'ENUM_HOST', 2: 'SCAN_PORT'},
'start_time': {0: 0.0, 1: 5.0, 2: 10.0}, 
'finish_time': {0: 5.0, 1: 10.0, 2: 35.0}, 
'duration': {0: 5.0, 1: 5.0, 2: 25.0},
'current_host': {0: -1, 1: -1, 2: 0}, 
'current_host_uuid': {0: -1, 1: -1, 2: '1381b434-3f3b-4b8a-a0b8-3583742eea6c'}, 
'compromise_host': {0: 'None', 1: 'None', 2: 'None'}, 
'compromise_host_uuid': {0: 'None', 1: 'None', 2: 'None'}, 
'current_host_attempt': {0: 0, 1: 0, 2: 1}, 
'cumulative_attempts': {0: 0, 1: 0, 2: 0}, 
'cumulative_compromised_hosts': {0: 0, 1: 0, 2: 0}, 
'compromise_users': {0: [], 1: [], 2: []}, 
'interrupted_in': {0: 'None', 1: 'None', 2: 'None'}, 
'interrupted_by': {0: 'None', 1: 'None', 2: 'None'},
} 
```
- Compromise checkpoint metrics
```json
[{
'time_to_compromise': 2372.763291073691,
'attack_success_rate': 0.38461538461538464,
'host_compromise_ratio': 0.1,
'mtd_execution_frequency': 0.005108120128305538
}, 
{
'time_to_compromise': 4009.0138625032932,
'attack_success_rate': 0.40816326530612246,
'host_compromise_ratio': 0.2,
'mtd_execution_frequency': 0.005108120128305538
}]
```

##### Response Elements
- `network` contains the graph of the network from the _network object. The `host` element of the nodes in the graph have been converted to json for compatibility with the [d3 library](https://d3js.org/).
- `mtd_record`and `attack_record` comprise the records of the total operation of the simulation, what attack and defense methods were utilised, as well as when and where.
- `compromise_checkpoint_metrics` contains some of the key metrics of the simulation at particular percentages of compromise.

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

