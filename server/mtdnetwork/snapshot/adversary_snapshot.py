import pickle
from mtdnetwork.component.adversary import Adversary
from mtdnetwork.snapshot import Snapshot


class AdversarySnapshot(Snapshot):
    def __init__(self):
        super().__init__()

    def save_adversary(self, adversary: Adversary, suffix=''):
        """
        saving adversary snapshot
        """
        file_name = self.get_file_by_suffix('adversary', suffix)
        with open(file_name, 'wb') as f:
            pickle.dump(adversary, f, pickle.HIGHEST_PROTOCOL)

    def load_adversary(self, suffix: str):
        """
        loading adversary based on saved snapshot
        """
        file_name = self.get_file_by_suffix('adversary', suffix)
        with open(file_name, 'rb') as f:
            adversary = pickle.load(f)
            return adversary
