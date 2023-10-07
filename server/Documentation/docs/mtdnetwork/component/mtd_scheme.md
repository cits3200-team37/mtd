# MTDScheme Class

#### Description

The `MTDScheme` class encapsulates the logic for different Moving Target Defense (MTD) schemes in a network environment. This class defines various MTD strategies, manages the registration and triggering of these strategies, and handles the suspension and activation of specific MTD techniques.

#### Initialization

- Parameters:
    - `scheme`: Specifies how MTDs are executed and can be done in `alternatively`, `simultaneously`, or `randomly`.
    - `network`: Refers to the simulation network.
    - `mtd_trigger_interval` (optional): The time interval to trigger MTD strategies. Defaults to None.
    - `mtd_trigger_std` (optional): Standard deviation for the trigger interval. Defaults to 0.5.
    - `custom_strategies` (optional): Custom MTD priority strategies for alternative or single schemes. Defaults to None.

- `_mtd_register_scheme`: A method that determines how MTD strategies are registered based on the chosen scheme.
- `_mtd_strategies`: A default list of available MTD strategies. `CompleteTopologyShuffle`, `IPShuffle`, `OSDiversity`, and `ServiceDiversity`.

#### Methods

`_init_mtd_scheme(scheme)`:

- Initializes the MTD scheme based on the provided `scheme`: `simultaneous`, `random`, `alternative` or `single`. This method sets the registration function for the MTD scheme. **WARN**: simultaneous and single scheme do not work

`_mtd_register(mtd)`:

- Registers a given MTD strategy to the network's queue. If the MTD passed is a class type, it instantiates it. The MTD strategy is paired with its priority and pushed onto the network's MTD queue.

`_register_mtd_simultaneously()`:

- Registers all custom MTD strategies for simultaneous execution.

`_register_mtd_randomly()`:

- Randomly selects and registers an MTD strategy from the custom strategies list.

`_register_mtd_alternatively()`:

- Registers custom MTD strategies in an alternative sequence.

`_register_mtd_single()`:

- Registers a single custom MTD strategy.

`trigger_suspended_mtd()`:

- Triggers the MTD strategy with the minimum priority from the suspended list

`trigger_mtd()`:

- Triggers the MTD strategy with the highest-priority from the network's MTD queue.

`suspend_mtd(mtd_strategy)`:

- Suspends a given MTD strategy, adding it to the network's suspended list based on its priority.

`register_mtd()`:

- Calls the appropriate MTD register scheme function based on the initialized scheme.

Getter Methods:
`get_scheme()`:

- Returns the MTD scheme type.

`get_mtd_trigger_interval()`:

- Returns the MTD trigger interval.

`get_mtd_trigger_std()`:

- Returns the standard deviation for the MTD trigger interval.

Setter Methods:

`set_mtd_strategies(mtd)`:

- Sets the MTD strategies list with the given strategies.

#### Dependencies

- mtdnetwork/mtd/completetopologyshuffle
- mtdnetwork/mtd/ipshuffle
- mtdnetwork/mtd/osdiversity
- mtdnetwork/mtd/servicediversity
- mtdnetwork/data/constants
