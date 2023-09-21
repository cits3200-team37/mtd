# User Shuffle

#### Description
usershuffle.py contains the `UserShuffle` class, a subclass of `MTD`.

- User Shuffle is an MTD strategy that randomly reassigns users to network hosts, which improves network security by making it more difficult for an attacker to predict what users are connected to specific hosts
- Parameters:
    - Takes optional `network` parameter, which the MTD strategy can be applied to

<br>
`mtd_operation` method

- This method loops through all the hosts of the network and reassigns a random user to each

#### Dependencies
- mtdnetwork/mtd



