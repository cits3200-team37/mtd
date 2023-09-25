# Host

#### Description

```host.py``` contains the ```Host``` class, a subclass of MTD.

- It is used to initialise the host with the specified Operating Sytems with a random network of internal services that the host runs.

- The internal service network for the Host maps what services the hacker needs to compromise in order to compromise the entire Host.

- A host is said to be compromised if a service adjacent to the target node is compromised or


- Parameters :
 - ```operating_system```: The operating system of the host

 - ```os_version```: The OS version

 - ```host_id```: The ID of the host on the graph of hosts
 - ```host_ip```:
                the IP address of the host
 - ```users_list```: A tuple list of Users on the Host that also specify if the user reuses their password eg. if Josh is added to this host and they reused their pass then users_list would be [("Josh", True)].
 - ```network```: The Network instance of the simulation
 - ```service_generator```: The ServiceGenerator instance for generating new services
 - ```k_nearest_neighbors_percent```: The ratio for the k nearest neighbors when generating the internal graph using Watts-Strogatz random graph
 - ```prob_strogatz_rewire```: The probability that an edge is rewired for the Watts-Strogatz random graph

- ```is_exposed_endpoint``` method
- ```get_all_services``` method
- ```get_test_values``` method
- ```get_total_nodes``` method
- ```get_all_vuln``` method
- ```get_vulns_for_list``` method
- ```swap_network``` method
- ```setup_network``` method
- ```set_compromised``` method
- ```possible_user_compromise``` method
- ```can_auto_compromise_with_users``` method
- ```is_compromised``` method
- ```compromise_with_users``` method
- ```get_service_and_vulns``` method
- ```get_target_node``` method
- ```get_exposed_nodes``` method
- ```remove_no_vuln_nodes``` method
- ```get_services``` method
- ```get_services_from_list``` method
- ```get_services_from_ports``` method
- ```port_scan``` method
- ```get_vulns``` method
- ```check_compromised``` method
- ```discover_neighbors``` method
- ```get_ports``` method
- ```get_ports_for_services``` method
- ```get_os_type_and_version``` method
- ```get_compromised_users``` method
- ```get_users``` method
- ```change_node_color``` method
- ```set_host_users``` method
- ```graph_choose_target_and_exposed``` method
- ```get_exposed_endpoints``` method
- ```gen_internal_network``` method
- ```draw``` method
- ```get_random_os_version``` method
- ```get_random_os``` method
- ```get_random_address``` method
- ```get_random_port``` method
- ```get_path_from_exposed``` method
- ```to_json``` method
#### Dependencies
