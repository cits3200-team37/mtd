# Service Diversity

#### Description
servicediversity.py contains the `ServiceDiversity` class, a subclass of `MTD`.

- Service Diversity is an MTD strategy seeking to diversify network services, making it more difficult for attackers to predict vulnerabilities
- Parameters:
    - Takes optional `network` parameter, which the MTD strategy can be applied to
    - Takes optional `shuffle` parameter defaulting to 50, which presumably determines the number of service shuffles, but does not appear to be used anywhere in the class


`mtd_operation` method

- This method changes the services of each host, provided the host is not an endpoint
- If the network is targeted (i.e., `get_network_type() == 0`), then the Attack Path Exposure Score is added to statistics for future use
- Takes an optional `adversary` parameter, however the code does not seem to use it
- *Note that the code systematically loops through host IDs and then randomly selects a host (`host_instance = random.choice(hosts)`); this is odd as no other similar MTD technique (e.g., OSdiversity, ipshuffle, etc.) does this*

#### Dependencies
- mtdnetwork/mtd



