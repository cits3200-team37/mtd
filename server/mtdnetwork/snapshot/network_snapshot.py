import pickle
from mtdnetwork.snapshot import Snapshot
from mtdnetwork.component.time_network import TimeNetwork


class NetworkSnapshot(Snapshot):
    def __init__(self):
        super().__init__()

    def save_network(self, network: TimeNetwork, suffix: str):
        """saving data related to generate the network graph"""
        file_name = self.get_file_by_suffix("network", suffix)
        with open(file_name, "wb") as f:
            pickle.dump(network, f, pickle.HIGHEST_PROTOCOL)

    def load_network(self, suffix: str):
        """loading data related to generate the network graph"""
        file_name = self.get_file_by_suffix("network", suffix)
        with open(file_name, "rb") as f:
            network = pickle.load(f)
            return network
