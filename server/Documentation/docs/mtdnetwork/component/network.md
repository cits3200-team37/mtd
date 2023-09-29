# Network Base Class

`network.py` is the basic network class, serving as the basis for all network super classes in the simulation.
#### Description

The `network` class is a data representation of a target network. It includes the basic attributes of networks and the methods to generate, update and manipulate it. This class serves as the basis on which the simulation is run.

#### Initialization

- Parameters:
    - `total_nodes`: The number of nodes in the network.
    - `total_endpoints`: The number of nodes exposed on the internet (hacker can interact directly with them).
    - `total_endpoints` must be less than total_nodes.
    - `total_subnets`: The number of sub-networks in the network
    - `total_layers`: The number of layers deep the network structures goes from the exposed endpoints.
    - `total_database`: The total size of the simulated database
    - `target_layer`: Sets the target layer where a target node will be selected.
    - `user_to_nodes_ratio`: The percent of users in comparison to host machines.
                each node will then be given `int(1/user_to_nodes_ratio)` users each (less users more users on each computer).
    - `prop_user_reuse_pass`: The probability that a user has reused their password.

- Properties:
    - `graph`: The network as a graph from the networkx library.
    - `colour_map`: A mapping of colours from constants.py to nodes based on sub-network.
    - `users_per_host`: The number of users per host on a node.
    - `total_users`: The total number of users.
    - `users_list`: A list of users.
    - `pos`: A dictionary of positions of items in the networks subgraphs.
    - `_database`: A list of the "database" containing values from `(total_nodes - total_database -> total_nodes)`.
    - `tags`: A list of Host tags from constants.py assigned to the networks layers.
    - `tag_priority`: An ordered list of tags by priority.
    - `service_generator`: A service_generator object from services.py.
    - `nodes`: A list of the nodes from total_nodes.
    - `mtd_strategies`: A list of mtd_strategies.
    - `reachable`: A list of reachable nodes.
    - `compromised_hosts`: A list of compromised hosts.
    - `node_per_layer`: A list of the number of nodes per layer.
    - `network_type`: An int specifying the attack type. 0 for targetted, 1 for general (no target node).
    - `vuln_dict`: A dictionary of Hosts and their vulnerabilities.
    - `vuln_count`: A dictionary vulnerabilities and their frequency in the network.
    - `service_dict`: A dictionary of hosts and their available services.
    - `service_count`: A dictionary of services and their frequency in the network.
    - `total_vuln`: The total number of vulnerabilities among hosts.
    - `total_services`: The total number of services among hosts.
    - `scorer`: A scorer object from `mtdnetwork.statistic.scorer`.
    - `target_node`: A target node for an attack.

#### Methods

- `init_network()`:
    initializes the network with its additional properties. Assigns tags, tag priority and users. Creates and sets up the network graph. Sets initial statistics.

- `update_host_information()`:
    Updates hosts networks to be itself.

- `gen_graph()`:

    Generates a network of subnets using the Barabasi-Albert Random Graph model.

    - Parameters:
        - `min_nodes_per_subnet`: The minimum number of computer nodes for each subnet. Default = 2.
        - `max_subnets_per_layer`: The maximum number of subnets per layer. Default = 5.
        - `subnet_m_ratio`: A ratio that is used to determine the parameter m for the barabasi albert graph. m is the number of edges to attach from a new node to existing nodes. Default = 0.2.
        - `prob_inter_layer_edge`: The probability that a node connects to a different layer in the network. Default = 0.4.

- `add_attack_path_exposure()`:
    Adds the Attack Path Exposure Score to statistics.
    
- `attack_path_exposure()`:
    Gets the total attack path exposure, scoring each node based on the % of new vulnerabilities found in each node on the shortest path to the target_node out of 1.

    - Returns:
        - ave_score: Score of each host added up, divided by the number of hosts.
    
- `setup_users()`:
    Randomly generates users that use the network.

    - Parameters:
        - `user_to_nodes_ratio`:
                the percent of users in comparison to host machines.
                each node will then be given `int(1/user_to_nodes_ratio)` users each (less users more users on each computer).
        - `prob_user_reuse_pass`:
                the probability that a user has reused their password.
        - `users_per_host`:
                how many users are allocated to each host on the network.

- `update_reachable_mtd()`:
    Updates the Reachable array with only compromised nodes that are reachable after MTD.

- `update_reachable_compromise()`:
    Updates the Reachable with the node_id of the compromised node.
    - Parameters:
        - `compromised_node_id`: id of the compromised node.
        - `compromised_hosts`: currently compromised hosts.

- `assign_tags()`:
     Assigns the tags to layers from constants.py.

- `assign_tag_priority()`:
    Orders tags based on priority.

- `sort_by_distance_from_exposed_and_pivot_host()`:
    Sorts the Host Stack by the shortest number of hops to reach the target hosts.

    - Parameters:
        - `host_stack`:
            a list of host IDs the attacker wants to attack.
        - `compromised_hosts`:
            a list of host IDs the hacker has compromised.
        - `pivot_host_id`:
            the ID of the host that is compromised that the hacker is using to pivot from. if None then it only sorts by the exposed endpoints. Default = -1 (no pivot)

- `setup_network()`:
    Using the generated graph, generates a host for each node on the graph.

- `is_target_compromised()`:
    Checks if the target node compromised.

    - Returns:
        boolean.

- `is_compromised()`:
    Checks if the Network has been completely compromised.

    - Parameters:
        `compromised_hosts`:
            the list of host IDs that have been compromised by the hacker.

    - Returns:
            boolean.
            
Getter Methods:

- `get_total_endpoints()`: Returns total endpoints.
- `get_exposed_endpoints()`: Returns exposed endpoints.
- `get_database()`: Returns database.
- `get_total_database()`: Returns total database.
- `get_scorer()`: Returns scorer.
- `get_statistics()`: Returns statistics from scorer.
- `get_service_generator()`: Returns service generator.
- `get_hosts()`: Returns hosts.
- `get_subnets()`: Returns subnets.
- `get_layers()`: Returns layers.
- `get_graph()`: Returns the network graph.
- `get_graph_copy()`: Returns a copy of the network graph.
- `get_pos()`: Returns pos (positions).
- `get_colourmap()`: Returns colour_map.
- `get_total_nodes()`: Returns total nodes.
- `get_network_type()`: Returns network type.
- `get_unique_subnets()`: Returns unique subnets.
- `get_reachable()`: Returns reachable nodes.
- `get_nodes_per_layer()`: Returns nodes per layer.
- `get_users_list()`: Returns users list.
- `get_users_per_host()`: Returns users per host.
- `get_host_id_priority()`: 
    Assign priority of host_id based on layer

    - Parameters:
        - `host_id`: node id of the desired node

    - Returns:
        `Priority`: An integer based on tag_priority array, with target node scoring 0, top priority node scoring 1, and subsequent nodes scoring 1 higher.
- `get_path_from_exposed()`:
    Gets the shortest path and distance from the exposed endpoints.

    Can also specify a subgraph to use for finding.

    - Parameters:
        - `target_node`:
            the target node to reach.
        - `graph`:
            subgraph of containing target. Default = `None`.

    - Returns:
            a tuple where the first element is the shortest path and the second element is the distance
        
- `get_shortest_distance_from_exposed_or_pivot()`: 
    Gets shortest distance to host from exposed hosts or a pivot host using get_path_from_exposed().

    - Parameters:
        - `host_id`:
            the target node to reach.
        - `pivot_host_id`:
            id of the pivot host. Default = -1 (no pivot)
        - `graph`:
            subgraph of containing target. Default = `None`.

    - Returns:
        Shortest distance.
- `get_neighbors()`:
    Returns the neighbours for a host.

    - Parameters:
        - `host_id`:
            the host ID to get the neighbors from

    - Returns:
        a list of the neighbors for the host.
- `get_hacker_visible_graph()`:
    Returns the Network graph that is visible to the hacker depending on the hosts that have already been compromised.
    
- `get_host()`:
    Gets the Host instance based on the host_id

    - Parameters:
        - `host_id`: the ID of the Host Instance

    - Returns:
        the corresponding Host instance
- `get_total_vulns()`: Returns total vulnerabilities.
- `get_vuln_dict()`: 
    Gets all the vulnerabilities for every hosts and puts them in vuln_dict

    - Returns:
        `vuln_count`: the frequency of every vuln
- `get_total_services()`: Returns total services.
- `get_service_dict()`:
    Gets all the services for every hosts and puts them in service_dict

    - Returns:
        - `service_count`: the freuqency of every service

#### Dependencies

    networkx
    pkg_resources
    matplotlib/pyplot
    numpy
    random
    os
    mtdnetwork/data/constants
    mtdnetwork/component/services
    mtdnetwork/component/host
    mtdnetwork/statistic/scorer
