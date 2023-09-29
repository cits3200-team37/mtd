# Complete Topology Shuffle

`completetopologyshuffle.py` contains the `CompleteTopologyShuffle` class, a subclass of `MTD`.

#### Description

The `CompleteTopologyShuffle` class is designed to completely regenerate the network graph while preserving the hosts from the previous state. This approach enhances unpredictability for potential adversaries by drastically altering the network structure.

#### Initialization

- Parameters:
    - `network` (optional): Specifies the network to be reshuffled. Expected to be an instance of a network class. Defaults to None.

#### Methods

`mtd_operation`:

- This method regenerates the network graph and integrates the previously existing hosts into the reshuffled network. The method updates reachable MTDs.
- If the network is targeted (i.e., `get_network_type() == 0`), then the Attack Path Exposure Score is added to statistics for future use
- Parameters:
    - `adversary` (optional): Defaults to None and the code does not seem to use it

#### Dependencies

- mtdnetwork/mtd
