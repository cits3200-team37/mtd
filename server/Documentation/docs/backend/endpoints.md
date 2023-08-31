# API Endpoints

## `[POST] /simulate`

Request body:

```
{
  "finishTime":int (optional),
  "mtdInterval":int,
  "scheme":string,
  "totalNodes":int,
  "seed": int (optional)
}
```

Sample request:

```json
{
  "finishTime": 3000,
  "mtdInterval": 200,
  "scheme": "random",
  "totalNodes": 100
}
```

Sample response:

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

This endpoint runs the `simulate_without_saving` function that can be found in `experiments/run.py`. It returns the resulting network of the simulation in a format that can be used with Javascript graphing library [d3](https://d3js.org/).

#### Request Parameters:

- `finishTime` is an optional parameter, if `finishTime` is not provided, the simulation runs till the network reaches compromised threshold (compromise ration > 0.9)
- `mtdInterval` is the time imterval ot trigger MTD(s)
- `scheme` is the mtd scheme to be used, please get available schemes from schemes endpoint TODO
- `totalNodes` is the number of nodes in the network (network size)
- `seed` can be provided to replicate simulations.
