from experiments.run import execute_simulation, create_experiment_snapshots
import logging
import matplotlib.pyplot as plt
from pathlib import Path

Path(Path.cwd() / "experimental_data" / "plots").mkdir(parents=True, exist_ok=True)
Path(Path.cwd() / "experimental_data" / "results").mkdir(parents=True, exist_ok=True)

logging.basicConfig(format="%(message)s", level=logging.INFO)

create_experiment_snapshots([25, 50, 75, 100])

evaluation = execute_simulation(
    start_time=0, finish_time=3000, mtd_interval=200, scheme="random", total_nodes=100
)

evaluation.get_network().draw()
plt.show()

evaluation.visualise_mtd_operation()

evaluation.visualise_attack_operation_group_by_host()

evaluation.visualise_attack_operation()

# Properties below return dataframes
evaluation.compromise_record_by_attack_action()
evaluation.compromise_record_by_attack_action("SCAN_PORT")
evaluation.compromise_record_by_attack_action("EXPLOIT_VULN")
evaluation.compromise_record_by_attack_action("BRUTE_FORCE")
evaluation.evaluation_result_by_compromise_checkpoint()
