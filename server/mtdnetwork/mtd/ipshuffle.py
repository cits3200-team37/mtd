'''Module contains MTD strategy that dynamically switches IP addresses of hosts'''
from mtdnetwork.mtd import MTD
from mtdnetwork.component import host


class IPShuffle(MTD):
    '''Subclass of MTD for IP shuffle MTD strategy'''
    def __init__(self, network=None):
        super().__init__(
            name="IPShuffle",
            mtd_type="shuffle",
            resource_type="network",
            network=network,
        )

    def mtd_operation(self, adversary=None):
        '''Method shuffles hosts of network'''
        hosts = self.network.get_hosts()

        ip_addresses = []
        for host_id, host_instance in hosts.items():
            if host_id in self.network.exposed_endpoints:
                continue
            host_ip = host.Host.get_random_address(existing_addresses=ip_addresses)
            ip_addresses.append(host_ip)
            host_instance.ip = host_ip
