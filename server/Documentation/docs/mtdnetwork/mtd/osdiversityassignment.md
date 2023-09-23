# OS Diversity Assignment

#### Description
osdiversityassignment.py contains 2 classes:

1. The `OSDiversityAssignment` class which is a subclass of `MTD`
2. The `DiversityAssignment` supporting class, which is used in a `OSDiversityAssignment` method 

---
`DiversityAssignment` class

- The class takes 6 parameters: `graph`, `sources`, `dests`, `os_types`, `pos`, `colour_map`; `pos` and `colour_map` are purely used for visualisations
- `gen_single_connection_graph` method: 
    -  This method removes nodes in source and destination nodes found in `sources` and `dests` parameters and appears to connect them to the source and destination nodes
    - It returns the modified graph
- `draw_dap_graph` method:
    - Purely for visualising the graph
- `calculate_variant_compromise_prob` method:
    - Takes a list of host IDs as `nodes` parameter
    - Calculates the mean compromise probability for OS type in `nodes`
- `objective` method:
    - This is the main method of the class; it effectively solves the OS diversity assignment by finding the optimal assignment of operating systems for a network graph

---
`OSDiversityAssignment` class

- The class relies on the `DiversityAssignment` class
- It is initialised with 2 parameters: `network`, the network that the MTD strategy is applies to, and `os_types`
- `mtd_operation` method:
    - Takes optional `adversary` parameter, which does not appear to be used in code
    - The method essentially assigns new operating system types and versions to each node of every host within the `network`

#### Dependencies
- mtdnetwork/mtd
- mtdnetwork.data.constants
- mtdnetwork.statistic.utils



