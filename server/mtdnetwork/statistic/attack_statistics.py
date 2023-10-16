'''Module for managing and recording data from attack operations'''
import os
import pandas as pd


class AttackStatistics:
    '''Class for recording attack data'''
    def __init__(self):
        self._attack_operation_record = []

    def append_attack_operation_record(
        self, name, start_time, finish_time, adversary, interrupted_mtd=None
    ):
        '''Method to append record of attack operation with relevant fields'''
        duration = finish_time - start_time
        interrupted_in = "None"
        interrupted_by = "None"
        uuid = -1
        if interrupted_mtd is not None:
            interrupted_in = interrupted_mtd.get_resource_type()
            interrupted_by = interrupted_mtd.get_name()
        if adversary.get_curr_host():
            uuid = adversary.get_curr_host().uuid

        self._attack_operation_record.append(
            {
                "name": name,
                "start_time": start_time,
                "finish_time": finish_time,
                "duration": duration,
                "current_host": adversary.get_curr_host_id(),
                "current_host_uuid": uuid,
                "compromise_host": "None",
                "compromise_host_uuid": "None",
                "current_host_attempt": adversary.get_attack_counter()[
                    adversary.get_curr_host_id()
                ],
                "cumulative_attempts": adversary.get_curr_attempts(),
                "cumulative_compromised_hosts": len(adversary.get_compromised_hosts()),
                "compromise_users": [],
                "interrupted_in": interrupted_in,
                "interrupted_by": interrupted_by,
            }
        )

    def update_compromise_host(self, curr_host):
        '''Method to update compromise host field with current host fields'''
        self._attack_operation_record[-1]["compromise_host"] = curr_host.host_id
        self._attack_operation_record[-1]["compromise_host_uuid"] = curr_host.uuid

    def update_compromise_user(self, user):
        '''Method to update compromise user field with most recent attack data'''
        self._attack_operation_record[-1]["compromise_users"].append(user)

    def get_record(self):
        '''Method returns attack operation record as pandas dataframe'''
        return pd.DataFrame(self._attack_operation_record)

    def save_record(self, sim_time, scheme):
        '''Method to save attack operation into CSV'''
        current_directory = os.getcwd()
        if not os.path.exists(current_directory + "/experimental_data/attack_records"):
            os.makedirs(current_directory + "/experimental_data/attack_records")
        pd.DataFrame(self._attack_operation_record).to_csv(
            "experimental_data/attack_records/attack_operation_record_"
            + str(sim_time)
            + "_"
            + scheme
            + ".csv",
            index=False,
        )
