'''Module for MTD class, the base class to MTD strategy subclasses'''
from mtdnetwork.data.constants import MTD_DURATION, MTD_PRIORITY

class MTD:
    '''Class of generic MTD strategy'''
    def __init__(self, name: str, mtd_type: str, resource_type: str, network=None):
        """
        :param name: name of the MTD strategy
        :param mtd_type: shuffle / diversity
        :param resource_type: application / network / reserve
        :param network: network object

        execution_time_mean: mean time for executing the implemented MTD strategy
        execution_time_std: std for executing the implemented MTD strategy
        priority: priority value of the implemented MTD strategy
        """
        self._name = name
        self._mtd_type = mtd_type
        self._resource_type = resource_type
        self._execution_time_mean = MTD_DURATION[name][0]
        self._execution_time_std = MTD_DURATION[name][1]
        self._priority = MTD_PRIORITY[name]
        self.network = network

    def __lt__(self, other):
        return self._priority < other.get_priority()

    def __gt__(self, other):
        return self._priority > other.get_priority()

    def __le__(self, other):
        return self._priority <= other.get_priority()

    def __ge__(self, other):
        return self._priority >= other.get_priority()

    def __str__(self):
        return (
            self._name
            + " "
            + self._resource_type
            + " "
            + str(self._execution_time_mean)
        )

    def mtd_operation(self, adversary=None):
        '''Placeholder for mtd_operation() method defined in subclasses'''
        raise NotImplementedError

    def get_mtd_type(self):
        '''Method returns mtd type'''
        return self._mtd_type

    def get_resource_type(self):
        '''Method returns resource type'''
        return self._resource_type

    def get_name(self):
        '''Method returns name of strategy'''
        return self._name

    def get_execution_time_mean(self):
        '''Method returns mean execution time'''
        return self._execution_time_mean

    def get_execution_time_std(self):
        '''Method returns standard deviation of execution time'''
        return self._execution_time_std

    def get_priority(self):
        '''Method returns priority'''
        return self._priority

    def set_priority(self, priority):
        '''Method assigns priority'''
        self._priority = priority
