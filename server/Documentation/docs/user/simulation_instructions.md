# MTD Simulator

## Moving Target Defence
Moving Target Defence (MTD) is a proposed mechanism to reduce the efforts of cyberattacks by continuously reconfiguring system components to increase uncertainty and complexity.

## Run Simulation
1. Launch MTD Simulator [app](./download_instructions.md) or open [web application](https://mtd.vercel.app/).
2. Navigate to [simulation](https://mtd.vercel.app/simulation) tab.
3. Input simulation parameters or choose a pre-set simulation scenario. 
4. Click `Submit` to generate network graph and summary graphs.

## Simulation Parameters

| Parameter       | Description                                                                         |
|-----------------|-------------------------------------------------------------------------------------|
| Scheme          | The manner in which the simulation will employ MTD strategies                       |
| MTD Interval    | The frequency that MTD strategies are applied                                       |
| Total Nodes     | The number of nodes in the simulated network                                        |
| Finish Time     | The maximum simulation duration                                                     |
| Total Endpoints | The number of endpoints in the simulated network                                    |
| Total Subnets   | The number of sub-networks in the simulated network, randomly spread between layers |
| Total Databases | The number of databases for the simulated network                                   |
| Total Layers    | The number of layers in the simulated network                                       |
| Target Layer    | The layer where the target node will be located on, if a targetted attack           |