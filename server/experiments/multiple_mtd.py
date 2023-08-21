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
from mtdnetwork.mtd.completetopologyshuffle import CompleteTopologyShuffle
from mtdnetwork.mtd.ipshuffle import IPShuffle
from mtdnetwork.mtd.osdiversity import OSDiversity
from mtdnetwork.mtd.servicediversity import ServiceDiversity
from mtdnetwork.mtd.osdiversityassignment import OSDiversityAssignment

warnings.filterwarnings("ignore")
plt.set_loglevel('WARNING')
from run import multiple_mtd_simulation, execute_multithreading
combination_mtds = [CompleteTopologyShuffle, IPShuffle, OSDiversity, ServiceDiversity, OSDiversityAssignment]

combination_list = []
for i in range(len(combination_mtds)):
    for j in range(i+1, len(combination_mtds)):
        combination_list.append((combination_mtds[i]().get_name() + " + " +
                                 combination_mtds[j]().get_name(),
                                 [combination_mtds[i], combination_mtds[j]]))

for combination_name, combination in combination_list:
    print(combination_name)
    results = execute_multithreading(multiple_mtd_simulation, iterations=100, num_threads=20,
                                     file_name=combination_name, combination=combination)
