# OS Diversity

#### Description
osdiversity. contains the `OSDiversity` class, a subclass of `MTD`.

- OS Diversity is an MTD strategy that seeks to diversify operating systems within a network in order to improve security
- Takes an optional `network` parameter, which the MTD strategy can be applied to

<br>
`mtd_operation` method

- This method changes the OS of existing hosts, iteratively updating the service should a node within the host not be compatible with the new OS
- If the network is targeted (i.e., `get_network_type() == 0`), then the Attack Path Exposure Score is added to statistics for future use
- Takes an optional `adversary` parameter, however the code does not seem to use it

#### Dependencies
- mtdnetwork/mtd
- mtdnetwork/data/constants



