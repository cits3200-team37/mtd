import os

current_directory = os.getcwd()


class Snapshot:
    def __init__(self):
        if not os.path.exists(current_directory + '/snapshots'):
            os.makedirs(current_directory + '/snapshots')

    @staticmethod
    def get_file_by_suffix(file_name: str, suffix: str):
        return current_directory + '/snapshots/' + file_name + '_' + suffix + '.pkl'
