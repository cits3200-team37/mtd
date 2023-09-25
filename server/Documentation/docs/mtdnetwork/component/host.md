# Host

#### Description

```host.py``` contains the ```Host``` class, a subclass of MTD.

- It is used to initialise the host with the specified Operating Sytems with a random network of internal services that the host runs.

- The internal service network for the Host maps what services the hacker needs to compromise in order to compromise the entire Host.

- A host is said to be compromised if a service adjacent to the target node is compromised or the hacker has been able to obtain the password for a user on the Host.

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

<br>

- ```is_exposed_endpoint``` method:
      - This method checks if the endpoint is exposed
- ```get_all_services``` method:
      - This method returns all the services
- ```get_test_values``` method:
      - This method returns all the services
- ```get_total_nodes``` method:
      - This method returns total number of nodes
- ```get_all_vuln``` method:
      - This method returns a list of the vulnerabilities
- ```get_vulns_for_list``` method:
      - This method retreives vulnerabilities for a given list
- ```swap_network``` method:
      - This method swaps the network
- ```setup_network``` method:
      - This method sets up the network configuration for the host
- ```set_compromised``` method:
      - This methods sets the host as compromised 


- ```possible_user_compromise``` method:

      - This method returns true if there is a user on the host that has reused their password.
  
-  ```can_auto_compromise_with_users``` method:

      - This method creates an action where the adversary tries to compromise the host using a reused password and returns an action that will return if the adversary was succesfully in finding a user with a reused password
      - Parameters:
          - compromised_users: a list of users the adversary has compromised
  
- ```is_compromised``` method:
     - This method return if the host is compromised 
  
- ```compromise_with_users``` method:

     - This method tries to brute force a login using the list of users that the adversary has compromised and returns and action if the brute force worked
     - Parameters:
          - ```compromised_users```: the list of users the hacker has compromised


- ```get_service_and_vulns``` method:

     - This method returns a dictionary of all non-target nodes and their vulnerabilities
    
- ```get_target_node``` method:

     - This method is used to get the target node


- ```get_exposed_nodes``` method:


    - This  method is used to get the exposed nodes


- ```remove_no_vuln_nodes``` method:

    - This method removes all service nodes with no vulnerabilities 


- ```get_services``` method:

    - This method gets the services on the host and returns a dictionary where the key is the ID and the value is the Service instance
    - Parameters:
          - ```just_exploited```: The services that have been exploited

- ```get_services_from_list``` method:
    
      - This method gets Service instance from a list of service numbers of host

- ```get_services_from_ports``` method:

    - This method is used to get the services from the discovered ports

- ```port_scan``` method:
     - This method is used to scan a port


- ```get_vulns``` method
  
     - This method gets the possible vulnerabilities on the Host based on the discovered port numbers and returns a hacer action for discovering if the vulnerabilities are present on the host and a possible method of exploitation
     - Parameters:
         - ```discovered_service_ports```: a list of ports found open doing a port scan
         - ```ignore_services```: the list of service IDs to ignore when searching for vulnerabilities
         - ```roa_threshold```: the return of attack (RoA) threshold that the adversary users for sorting the exploits they want to use

  
- ```check_compromised``` method:
  
     - This method checks if the current host is compromised
  
- ```discover_neighbors``` method:

     - This method scans for neighbours of the host and returns an action that returns a list of neighbouring host ids.
- ```get_ports``` method:
  

     - This method returns all the ports on he host

- ```get_ports_for_services``` method:

     - This methods is used to get a list of ports associated with specified services
  
- ```get_os_type_and_version``` method:
     - This method is used to get the OS type and version
 
- ```get_compromised_users``` method:
 
     - This method is used to retreive a list of compromised users.

- ```get_users``` method:
     - This method is used to retreive a list of users 
  
- ```change_node_color``` method:
     
     - This  method changes the color of the host on the overall network
  
- ```set_host_users``` method:
     - This method sets the users on the host.
     - Parameters:
         - ```users_list```: The tuple users lists specifying the username and if the user reuses their password
  
- ```graph_choose_target_and_exposed``` method:

     - This method chooses the target and exposed services on the internal network.TThe exposed services means that an adversary can see the ports open externally
     - Parameters:
         - ```graph```: The graph that is being generated.
         - ```target_distance```: The target distance from the target node for exposed services.

- ```get_exposed_endpoints``` method:

     - This method is used to get the exposed endpoints.
  
- ```gen_internal_network``` method:

     - This method is used to generate the internal network.

- ```draw``` method:

     - This method is used to draw the internal network for the host


- ```get_random_os_version``` method:

     - This method gets a random Operating System version.The latest versions are more likely to be chosen over older and outdated OS versions.
     - Parameters:
         - ```operating_system```: The name of the operating_system to pick a random version for.


- ```get_random_os``` method:
     - This method returns a random OS
     
- ```get_random_address``` method:
  
     - This method gets a Random IPv4 address and makes sure that one does not already exist.
     - Parameters:
         -```existing_addresses```: A list of already allocated IP addresses on the network



- ```get_random_port``` method:

     - This method gets a random port while checking a port has already been allocated for a host.
     - Parameters:
         - ```existing_ports```: The port numbers that have already been allocated to the host


- ```get_path_from_exposed``` method:
     - This method gets the shortest path and distance from the exposed endpoints and returns a tuple where the first element is the shortest path and the second element is the distance
 

- ```to_json``` method:

     - This method converts host attributes to a JSON representation
  
#### Dependencies
- mtdnetwork/data/constants
- import mtdnetwork/component/services
- import mtdnetwork/component/time_network 