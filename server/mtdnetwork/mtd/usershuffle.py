"""Module of MTD strategy that randomly reassigns users to network hosts"""
import random
from mtdnetwork.mtd import MTD


class UserShuffle(MTD):
    """Class to implement MTD strategy"""

    def __init__(self, network=None):
        super().__init__(
            name="UserShuffle",
            mtd_type="shuffle",
            resource_type="reserve",
            network=network,
        )

    def mtd_operation(self, adversary=None):
        hosts = self.network.get_hosts()

        for host_instance in hosts.values():
            host_instance.set_host_users(
                random.choices(self.network.users_list, k=self.network.users_per_host)
            )
