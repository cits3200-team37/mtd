# Service Class

## Vulnerability Class

#### Description

The `Vulnerability` class defines a vulnerability's properties such as its complexity, impact, and associated CVSS score. It also handles certain behaviors like calculating the time required to exploit the vulnerability and determining if it has been exploited.

#### Initialization

- Parameters:

    - `can_have_os_dependency` (optional): Specifies if the vulnerability can have an OS dependency. Defaults to False.
    - `os_list` (optional): A list of operating systems that the vulnerability might be applicable to, depending on the service.

- `complexity`: A float value (between `VULN_MIN_COMPLEXITY` and 1) representing how hard it is to exploit this vulnerability, with 1 being easy and 0 being impossible.
- `impact`: A float value (between 0 and 10) representing the severity of successfully exploiting this vulnerability.

#### Methods

`is_exploited`:

- Return if the vulnerability has been exploited.

`get_id`:

- Return the unique identifier of the vulnerability.

`can_exploit_with_dependent_vuln`:

- checks if there is another vulnerability in the provided list that, when exploited, can enable the exploitation of the current vulnerability. The function return True if such a vulnerability exists in `vulns` or if the current vulnerability has no dependencies.

`exploit_time`:

- Calculates the time required to exploit this vulnerability. This estimate is influenced by the vulnerability's complexity, its potential operating system dependency, and whether it's already been exploited.

`network`:

- Tries to exploit the vulnerability. If the vulnerability has already been exploited, it returns the impact score directly. Otherwise, it checks factors like complexity and operating system dependencies to determine the success of the exploitation. The method either returns the impact score upon successful exploitation or 0.0 if the attempt fails. It returns the impact score upon successful exploitation or 0.0 if the attempt fails.

`roa`:

- Computes a pseudo "return on attack" metric that assesses the potential gain of an attack in relation to its cost, using the exploit time as the cost

`initial_roa`:

- Calculates the initial "return on attack" metric using a predefined minimum exploit time.

`__eq__`:

- Determines if two instances of the Vulnerability class are equal based on their unique IDs.

## Service Class

#### Description

The `Service` class encapsulates properties related to a particular software service, including its name, version, and associated vulnerabilities. The class provides methods for accessing vulnerabilities based on specific criteria and assessing whether the service has been exploited based on its vulnerabilities.

#### Initialization

- Parameters:

    - `service_name`: The name of the service.
    - `service_version`: The version of the service.
    - `vulnerabilities`: A list of vulnerabilities associated with the service.

- `exploit_value`: Initialized to 0.0, it represents the accumulated impact of exploited vulnerabilities on the service.
- `id`: A unique identifier for the service instance.

#### Methods

`copy`:

- Return a new `Service` instance that is a copy of the current instance, including its name, version, and vulnerabilities.

`get_vulns`:

- Provides the top vulnerabilities of the service based on their RoA values, excluding already exploited vulnerabilities. It can optionally take a RoA threshold and return only those vulnerabilities with a RoA greater than the threshold. By default, it returns a maximum of `SERVICE_TOP_X_VULNS_TO_RETURN` vulnerabilities.

`get_all_vulns`:

- Return the complete list of vulnerabilities associated with the service.

`get_id`:

- Return the unique identifier of the service instance.

`is_exploited`:

- Determines if the service has been exploited by evaluating the sum of the impact values of its exploited vulnerabilities. The service is considered exploited if this sum exceeds the `SERVICE_COMPROMISED_THRESHOLD`.

`discover_vuln_time`:

- Calculates the time required to discover vulnerabilities in the service based on the number of vulnerabilities surpassing a given RoA threshold. It uses the constant `SERVICE_DISCOVER_EACH_VULN_TIME` to determine the discovery time for each vulnerability.

`get_highest_roa_vuln`:

- Return the RoA value of the top vulnerability of the service in terms of RoA, or 0.0 if there are no vulnerabilities that meet the criteria.

`__eq__`:

- Compares the current `Service` instance with another object to determine equality. Two services are considered equal if they have the same name and version.

## ServicesGenerator Class

#### Description

The `ServicesGenerator` class is responsible for generating services for the simulation. It determines the distribution of services across various operating systems, models vulnerabilities for each service, and calculates the compatibility of services with different OS versions.

#### Initialization

- Parameters:
    - `services_per_os` (optional): The number of services assigned to each OS. Defaults to `constants.SERVICE_NO_OF_SERVICES_PER_OS`.
    - `percent_cross_platform` (optional): Percent of services available across all platforms. Defaults to `constants.VULN_PERCENT_CROSS_PLATFORM`.
    - `max_vuln_probability` (optional): Maximum probability for older service versions having a vulnerability. Defaults to `constants.VULN_MAX_PROB_FOR_OCCURING_FOR_SERVICE_VERSION`.
    - `vuln_patch_mean` (optional): Average number of versions it takes for a vulnerability to be patched. Defaults to `constants.VULN_PATCH_MEAN`.
    - `vuln_patch_range` (optional): Range from the `vuln_patch_mean`. Defaults to `constants.VULN_PATCH_RANGE`.
    - `vuln_initial_chances` (optional): For the first service version, it iterates `vuln_initial_chances` times, testing if the first service gets a new vulnerability. Defaults to `constants.VULN_INITIAL_CHANCES`.
    - `os_dependent_vuln_chance` (Unused): Probability of a vulnerability being enabled only on a specific OS (if the service is available across platforms). Defaults to `constants.VULN_PROB_DEPENDS_ON_OS`.
    - `dependent_vuln_chance` (Unused): Chance that a vulnerability can be exploited only if there's another specific type of vulnerability present. Defaults to `constants.VULN_PROB_DEPENDS_ON_OTHER_VULNS`.

#### Methods

`get_random_service`:

- Selects a random service for a specified OS type and version and returns it.

`get_random_service_latest_version`:

- Fetches a random service, set to the latest version for the given OS type and version.

`service_is_compatible_with_os`:

- Checks if a service is compatible with a particular OS type and version. Returns True if compatible, False otherwise.

`gen_services`:

- This method is responsible for generating services, their associated vulnerabilities, and distributing them across different operating system types and versions.

`get_service_name_list`:

- Static method. Retrieves a list of service names.

`get_all_generated_services`:

- Fetches all the generated services for the simulation.

## Dependencies

- mtdnetwork/data/constants
