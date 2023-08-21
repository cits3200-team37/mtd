import os
import sys

current_directory = os.getcwd()
if not os.path.exists(current_directory + '/experimental_data'):
    os.makedirs(current_directory + '/experimental_data')
    os.makedirs(current_directory + '/experimental_data/plots')
    os.makedirs(current_directory + '/experimental_data/results')
sys.path.append(current_directory.replace('experiments', ''))
import warnings
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
plt.set_loglevel('WARNING')
from run import single_mtd_simulation, execute_multithreading, create_experiment_snapshots

create_experiment_snapshots([25, 50, 75, 100])


results = execute_multithreading(single_mtd_simulation, iterations=100, num_threads=20, file_name='single_mtd_sim')
