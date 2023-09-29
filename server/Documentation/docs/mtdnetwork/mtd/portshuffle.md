# Port Shuffle

#### Description
portshuffle.py contains the `PortShuffle` class, a subclass of `MTD`.

- Port Shuffling is an MTD strategy that dynamically changes the ports associated with network services in order to decrease network predictability for attackers
- Takes an optional `network` parameter, which the MTD strategy can be applied to

`mtd_operation` method

- This method carries out the port shuffling on a particular network, updating the port of all nodes in a host should the host not be an endpoint
- Takes an optional `adversary` parameter, however the code does not seem to use it

#### Dependencies
- mtdnetwork/mtd
- mtdnetwork/component/host



