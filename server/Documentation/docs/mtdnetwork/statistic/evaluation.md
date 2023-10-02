# Evaluation
The `Evaluation` class in `evaluation.py` serves to derive useful statistics from the `Network` and `Adversary` objects of the simulation.
#### Description
The `Evaluation` class mainly compiles the statistics data stored in the `Network` and `Adversary` objects into graphs and summarized metrics for human viewing using matplotlib.

#### Initialization
- Parameters
    - `network`: a network object (usually `time_network`), typically of the final state of the simulation.
    - `adversary`: an adversary object, typically of the final state of the simulation.

#### Properties
- `network`: Network object.
- `adversary`: Adversary object.
- `mtd_record`: MTD statistics from the network object.
- `attack_record`: Attack statistics from the adversary object.

#### Methods

- `compromised_num()`:
    - Parameters
        - `record`: an attack record.

    - Returns:
        - Number of compromised hosts.

- `mtd_execution_frequency()`:
    The frequency of executing MTDs.
    - Returns: Total number of executed MTD / Elapsed time.

- `evaluation_result_by_compromise_checkpoint()`:
    Metrics at compromise checkpoints (% compromise)
    - Parameters:
        - `checkpoint`: an array of decimal compromise ratios (i.e. 0.1).
    
    - Returns:
        - an array of dictionaries of compromise ratios and metrics
        - { <br>
            `"time_to_compromise"`, <br>
            `"attack_succes_rate"`, <br>
            `"host_compromise_ratio"`, <br>
            `"mtd_execution_frequency"` <br>
        }
- `compromise_record_by_attack_action()`:
    - Parameters:
        - `action`: a specified attack action.
    - Returns:
        - a list containing hosts compromised by the given action.
    
- `draw_network()`:
    Draws the topology of the network while also highlighting compromised and exposed endpoint nodes.

-   `draw_hacker_visible()`:
    Draws the network that is visible for the hacker.

-   `draw_compromised()`:
    Draws the network of compromised hosts.

-   `visualise_attack_operation_group_by_host()`:
    Visualises the action flow of attack operations by host ids.

-   `visualise_attack_operation()`:
    Visualises the action flow of attack operations by attack type.

-   `visualise_mtd_operation()`:
    Visualises the action flow of mtd operations.

#### Getter Methods

-   `get_network()`: Returns network object.
#### Dependencies

- `numpy`
- `matplotlib/pyplot`
- `matplotlib/lines`
- `networkx`
- `pandas`
- `os`