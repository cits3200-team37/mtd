"""Module for recording data related to MTD strategies"""
import os
import pandas as pd


class MTDStatistics:
    """Class for recording statistics of MTD strategies"""

    def __init__(self):
        self._mtd_operation_record = []
        self._total_suspended = 0
        self._total_triggered = 0
        self._total_executed = 0
        self._total_attack_interrupted = 0
        self._switch_mtd_interval_at = {}
        self._switch_mtd_strategy_at = {}

    def append_mtd_operation_record(
        self, mtd_strategy, start_time, finish_time, duration
    ):
        """Method appends data to record"""
        self._mtd_operation_record.append(
            {
                "name": mtd_strategy.get_name(),
                "start_time": start_time,
                "finish_time": finish_time,
                "duration": duration,
                "executed_at": mtd_strategy.get_resource_type(),
            }
        )
        self._total_executed += 1

    def append_mtd_interval_record(self, timestamp, mtd_interval):
        """Method records mtd interval at particular timestamp"""
        self._switch_mtd_interval_at[timestamp] = mtd_interval

    def append_mtd_strategy_record(self, timestamp, mtd_strategy):
        """Method records mtd strategy used at particular timestamp"""
        self._switch_mtd_strategy_at[timestamp] = mtd_strategy

    def dict(self):
        """Method returns dictionary containing statitsics related to mtd"""
        return {
            "Total suspended MTD": self._total_suspended,
            "Total executed MTD": self._total_executed,
            "Total attack interrupted": self._total_attack_interrupted,
            "Switch MTD interval at": self._switch_mtd_interval_at,
            "Switch MTD strategy at": self._switch_mtd_strategy_at,
        }

    def add_total_attack_interrupted(self):
        """Method increments count of attacks interrupted"""
        self._total_attack_interrupted += 1

    def add_total_suspended(self):
        """Method increments count of suspended mtd strategies"""
        self._total_suspended += 1

    def add_total_triggered(self):
        """method increments count of total triggered mtd strategies"""
        self._total_triggered += 1

    def get_record(self):
        """Method returns mtd record as pandas dataframe"""
        return pd.DataFrame(self._mtd_operation_record)

    def save_record(self, sim_time, scheme):
        """Method saves MTD records in csv file"""
        current_directory = os.getcwd()
        if not os.path.exists(current_directory + "/experimental_data/mtd_records"):
            os.makedirs(current_directory + "/experimental_data/mtd_records")
        pd.DataFrame(self._mtd_operation_record).to_csv(
            "experimental_data/mtd_records/mtd_operation_record_"
            + str(sim_time)
            + "_"
            + scheme
            + ".csv",
            index=False,
        )

    def get_total_attack_interrupted(self):
        """Method returns total attacks interrupted by mtd strategies"""
        return self._total_attack_interrupted
