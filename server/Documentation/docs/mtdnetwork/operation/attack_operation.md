# Attack Operation

#### Description
attack_operation.py contains the 'UserShuffle' class, a subclass of 'MTD'

 - Used to initalize a new attack operation

execute_operation method:

 - This method is used to execute a given time-consuming attack action. The method has two parameters:
 - time - The time duataion before executing an attack action
 - attack_action - attack action

scan_host method:

 - This method is used to raise a SCAN_HOST action

_enum_host method:

  - This method is used to raise a ENUM_HOST action

_exploit_vuln method:

  - This method is used to raise an EXPLOIT_VULN action

_brute_force method:

  - This method is used to raise an BRUTE_FORCE action

_scan_neighbours method:

  - This method is used to raise a SCAN_NEIGHBOUR action

_handle_interrupt method:

  - This method is used to handle the interrup of the attack action caused by the MTD operations. The method has two parameters:
  - start_time: the start time of th action
  - name: the name of the attack action

_execute_enum_host method:

 - This method starts enumeratinf each host by pooping off the host id from the top of the host stack. The time for host hopping is required.
 - This method also checks if the hacker has already compormised and backdoored the target host

_execute_scan_port method:
  - Starts a port scan on the target host and checks if a compormised user has reused their credentials on the target host 
  
_execute_exploit_vuln method:

   - This method finds the top 5 vulnerbilities based on RoA score and tries exploiting the vulneribilities to compormise the host.

_execute_brute_force method:

   - This method tries bruteforcinf a login for a short perios of time using previous passwords from compromised user accounts to guess a new login.
   - This method also id credentails for a user account has been succefully compromised

_execute_scan_neighbour method:

  - This method starts scanning fro neighbuors for a host that the hack can pivot to and puts the new neighbours discovered to the stars of the host stack.

_sect_next_pivot_host method:
  
  - This method sets the next host that the hacker will pivor from to compormise other hosts. The pivot host needs to be a comprmoised host the hack can access

update_compromise_method method:

  - This method updates the hacker's progress state when it compromises a host

get_proceed_time method:

  - This method returns the proceed time

set_proceed_time method:

  - This method sets the proceed time

get_attack_process method:

  - This method returns the attack process

set_attack_ process method:

  - This method sets the attack process

set_interrupted_mtd method:

  - This method sets the interrupted MTD operation

get_adversary method:

  - This method returns the adversary 


#### Dependencies

