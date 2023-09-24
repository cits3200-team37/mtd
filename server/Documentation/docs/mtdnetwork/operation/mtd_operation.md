# MTD Operation Class

`MTDOperation` is the main class for the execution and management of Moving Target Defense (MTD) strategies during network simulations.

#### Description

The `MTDOperation` class encapsulates the functionality required to execute, suspend, trigger, and manage MTD strategies within a network. It interacts with the network environment and use the simpy library for manage these events. The class determines when to deploy a strategy, how to handle resource conflicts, and manages MTD registration and suspension.

#### Initialization

- Parameters:
    - `env`: Facilitates the simpy environment framework.
    - `end_event`: Marks the end of a simulation event.
    - `network`: Refers to the simulation network.
    - `attack_operation`: Represents the attack operation in the network.
    - `scheme`: Specifies how MTDs are executed and can be done in  `alternatively`, `simultaneously`, or `randomly`.
    - `proceed_time` (optional): Time to progress MTD simulation. Defaults to 0.
    - `mtd_trigger_interval` (optional): The time interval to trigger MTD strategies. Defaults to None.
    - `custom_strategies` (optional): Custom MTD priority strategies for alternative or single schemes. Defaults to None.

- Several `simpy.Resource` instances represent resources like application layer, network layer, and a reserve for potential MTD execution.

#### Methods

`proceed_mtd`:

- Initiates the MTD process, checking for unfinished MTDs and suspending them. Decides the MTD scheme (batch or individual) to trigger.

`_mtd_trigger_action`:

- The core function for triggering individual MTD strategies at exponential time intervals. It checks for network compromise and then decides to either register, trigger, or suspend an MTD strategy based on resource occupation conditions.

`_mtd_batch_trigger_action`:

- This function triggers the suspended MTDs based on priority if available, otherwise registers and triggers all MTDs simultaneously. It continuously checks if the network is compromised and decides to either register, trigger, or suspend MTDs in batches based on resource occupation. Then, It waits for an exponentially distributed time interval before initiating the next round of MTD operations.

`_mtd_execute_action`:

- This function is an action for executing an MTD strategy. Once an MTD is deployed, it waits for a certain period, checks for network compromise, and then executes the MTD. After execution, it logs necessary details, releases the occupied resource, and interrupts the adversary's operation if required.

`_get_mtd_resource`:

- Given an MTD, this function determines which resource (network, application, or reserve) the MTD will occupy or use.

`_interrupt_adversary`:

- This function interrupts the adversary's attack process based on the type of MTD triggered and the current attack process. If there's an ongoing attack process and the MTD affects the `network` resource, the function interrupts the attack process irrespective of its type. If the MTD affects the `application` resource, the function will only interrupt the adversary's attack if the attack isn't in the processes of `SCAN_HOST`, `ENUM_HOST`, or `SCAN_NEIGHBOR`.

Getter Methods:

- `get_proceed_time()`: Returns the time taken to progress the MTD simulation.
- `get_application_resource()`: Retrieves the application layer resource.
- `get_network_resource()`: Retrieves the network layer resource.
- `get_reserve_resource()`: Retrieves the reserve resource.
- `get_mtd_scheme()`: Returns the current MTD scheme in use.

#### Dependencies

- mtdnetwork/component/time_generator
- mtdnetwork/data/constants