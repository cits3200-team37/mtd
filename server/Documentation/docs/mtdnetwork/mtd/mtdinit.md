# MTD Base Class

`__init__.py` introduces the foundational `MTD` class, serving as the base for all Moving Target Defense (MTD) strategies in the network.

#### Description

The `MTD` class is a generic representation of an MTD strategy. It includes essential attributes and methods that any MTD strategy should use. This base class is crucial for maintaining a consistent structure and interface across different MTD strategies.

#### Initialization

- Parameters:
    - `name`: Name of the MTD strategy.
    - `mtd_type`: Categorized either as "shuffle" or "diversity".
    - `resource_type`: Defines whether the MTD is related to an "application", "network", or is in "reserve".
    - `network` (optional): Specifies the network to be reshuffled. Expected to be an instance of a network class. Defaults to None.
- Properties:
    - `execution_time_mean`: Average time taken to execute the MTD strategy.
    - `execution_time_std`: Standard deviation of the time taken to execute the MTD strategy.
    - `priority`: Priority level of the MTD strategy.

#### Methods

Comparison Operators (`__lt__`, `__gt__`, `__le__`, `__ge__`):

- Enable the comparison of MTD strategy objects based on their priority levels.

`__str__`:

- Returns a formatted string providing a concise representation of the MTD strategy.

`mtd_operation`:

- A placeholder method for implementing the specific operations of a MTD strategy. Raises a `NotImplementedError` in this base class.

Getter Methods:

- `get_mtd_type()`: Returns the type of MTD.
- `get_resource_type()`: Returns the resource type.
- `get_name()`: Returns the name of the MTD strategy.
- `get_execution_time_mean()`: Returns the average execution time.
- `get_execution_time_std()`: Returns the execution time's standard deviation.
- `get_priority()`: Returns the priority of the MTD strategy.

Setter Method:

- `set_priority(priority)`: Sets the priority of the MTD strategy.

#### Dependencies

- mtdnetwork/data/constants
