# Complete Topology Shuffle

`hosttopologyshuffle.py` contains the `HostTopologyShuffle ` class, a subclass of `MTD`.

#### Description

The HostTopologyShuffle class provides functionality to swap hosts within the network. This shuffle introduces unpredictability to potential adversaries by altering the positions of hosts within the network's structure.

#### Initialization

- Parameters:
  - `network` (optional): Specifies the network to be reshuffled. Expected to be an instance of a network class. Defaults to None.

#### Methods

`random_different_host_id`:

- This function provides a randomly chosen host ID from a list that is different from the given current host ID.
- Parameters:
    - `curr_host_id`: Current host's ID.
    - `hosts_list`: A list of host IDs.

`mtd_operation`:

- This method conducts the host shuffle operation by swapping the host IDs between different nodes in the network graph. While doing this, it ensures that exposed endpoints remain unaffected. 
- After the shuffle, the method updates reachable MTDs
- If the network is targeted (i.e., `get_network_type() == 0`), then the Attack Path Exposure Score is added to statistics for future use
- Parameters:
    - `adversary` (optional): Defaults to None and the code does not seem to use it

#### Dependencies

- mtdnetwork/mtd
