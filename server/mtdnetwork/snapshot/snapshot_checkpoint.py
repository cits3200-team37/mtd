from mtdnetwork.snapshot.network_snapshot import NetworkSnapshot
from mtdnetwork.snapshot.adversary_snapshot import AdversarySnapshot
from collections import deque


class SnapshotCheckpoint:

    def __init__(self, env=None, checkpoints=None):
        self.env = env
        self._proceed_time = 0
        self._checkpoint_stack = checkpoints

    def proceed_save(self, time_network, adversary):
        """launch an event in simulation to save snapshots by time"""
        if self._checkpoint_stack is not None:
            self._checkpoint_stack = deque(self._checkpoint_stack)
        self.env.process(self.save_snapshots_by_time(time_network, adversary))

    def save_snapshots_by_time(self, time_network, adversary):
        """
        :param time_network: network object to save
        :param adversary: adversary object to save
        """
        last_checkpoint = self._proceed_time
        while len(self._checkpoint_stack) > 0:
            checkpoint = self._checkpoint_stack.popleft()
            if checkpoint < last_checkpoint:
                continue
            yield self.env.timeout(checkpoint - last_checkpoint)
            last_checkpoint = checkpoint
            NetworkSnapshot().save_network(time_network, str(self.env.now + self._proceed_time))
            AdversarySnapshot().save_adversary(adversary, str(self.env.now + self._proceed_time))

    def load_snapshots_by_time(self, time):
        self.set_proceed_time(time)
        time_network = NetworkSnapshot().load_network(str(time))
        adversary = AdversarySnapshot().load_adversary(str(time))
        return time_network, adversary

    @staticmethod
    def load_snapshots_by_network_size(size):
        time_network = NetworkSnapshot().load_network(str(size)+'n')
        adversary = AdversarySnapshot().load_adversary(str(size)+'n')
        return time_network, adversary

    @staticmethod
    def save_snapshots_by_network_size(time_network, adversary):
        NetworkSnapshot().save_network(time_network, str(time_network.get_total_nodes()) + 'n')
        AdversarySnapshot().save_adversary(adversary, str(time_network.get_total_nodes()) + 'n')

    def save_initialised(self, time_network, adversary):
        NetworkSnapshot().save_network(time_network, str(self._proceed_time))
        AdversarySnapshot().save_adversary(adversary, str(self._proceed_time))

    def set_proceed_time(self, proceed_time):
        self._proceed_time = proceed_time

