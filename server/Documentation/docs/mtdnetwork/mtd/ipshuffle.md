# IP Shuffle

#### Description
ipshuffle.py contains the `IPShuffle` class, a subclass of `MTD`.

- IP Shuffle is an MTD strategy that dynamically switches IP addresses of hosts to improve network security (e.g., it invalidates IP address collection by attacker)
- Takes an optional `network` parameter, which the MTD strategy can be applied to

<br>
`mtd_operation` method

- Shuffles IP of host to a random address, if host is not an exposed endpoint
- Takes an optional `adversary` parameter, however the code does not seem to use it

#### Dependencies
- mtdnetwork/mtd
- mtdnetwork/component/host



