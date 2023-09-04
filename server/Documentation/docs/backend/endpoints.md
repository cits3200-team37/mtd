# API Endpoints

## `[POST] /simulate`

#### Description

This endpoint runs the `simulate_without_saving` function that can be found in `experiments/run.py`. It returns the resulting network of the simulation in a format that can be used with Javascript graphing library [d3](https://d3js.org/).

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
- `checkpoints` is a list of time value to save snapshots as simulation runs
    - Stable test limit: No apparent limit (even negative integers do not produce an error)
    - Logical limit: Positive integers
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
- `newNetwork` is a boolean value; `True` creates new snapshots based on network size, `False` loads snapshots based on network size

