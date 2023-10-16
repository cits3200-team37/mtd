import simpy
from mtdnetwork.component.time_network import TimeNetwork
from mtdnetwork.operation.mtd_operation import MTDOperation
from mtdnetwork.data.constants import ATTACKER_THRESHOLD
from mtdnetwork.component.adversary import Adversary
from mtdnetwork.operation.attack_operation import AttackOperation
from mtdnetwork.statistic.evaluation import Evaluation
from mtdnetwork.mtd import MTD


def run_simulation(
    start_time=0,
    finish_time=None,
    scheme="random",
    mtd_interval=None,
    custom_strategies: MTD | list[MTD] = None,
    total_nodes=50,
    total_endpoints=5,
    total_subnets=8,
    total_layers=4,
    target_layer=4,
    total_database=2,
    seed=None,
):
    """

    :param start_time: the time to start the simulation, need to load timestamp-based snapshots if set start_time > 0
    :param finish_time: the time to finish the simulation. Set to None will run the simulation until
    the network reached compromised threshold (compromise ratio > 0.9)
    :param scheme: random, simultaneous, alternative, single, None
    :param mtd_interval: the time interval to trigger an MTD(s)
    :param custom_strategies: used for executing alternative scheme or single mtd strategy.
    :param checkpoints: a list of time value to save snapshots as the simulation runs.
    :param total_nodes: the number of nodes in the network (network size)
    :param total_endpoints: the number of exposed nodes
    :param total_subnets: the number of subnets (total_nodes - total_endpoints) / (total_subnets - 1) > 2
    :param total_layers: the number of layers in the network
    :param target_layer: the target layer in the network (for targetted attack scenario only)
    :param total_database: the number of database nodes used for computing DAP algorithm
    :param new_network: True: create new snapshots based on network size, False: load snapshots based on network size
    """
    if total_endpoints is None:
        total_endpoints = 5
    if total_subnets is None:
        total_subnets = 8
    if total_layers is None:
        total_layers = 4
    if target_layer is None:
        target_layer = 4
    if total_database is None:
        total_database = 2

    # initialise the simulation
    env = simpy.Environment()
    end_event = env.event()

    time_network = None
    adversary = None

    time_network = TimeNetwork(
        total_nodes=total_nodes,
        total_endpoints=total_endpoints,
        total_subnets=total_subnets,
        total_layers=total_layers,
        target_layer=target_layer,
        total_database=total_database,
        seed=seed,
    )

    adversary = Adversary(network=time_network, attack_threshold=ATTACKER_THRESHOLD)

    # start attack
    attack_operation = AttackOperation(
        env=env, end_event=end_event, adversary=adversary, proceed_time=0
    )
    attack_operation.proceed_attack()

    # start mtd
    if scheme is not None:
        mtd_operation = MTDOperation(
            env=env,
            end_event=end_event,
            network=time_network,
            scheme=scheme,
            attack_operation=attack_operation,
            proceed_time=0,
            mtd_trigger_interval=mtd_interval,
            custom_strategies=custom_strategies
            if scheme != "single"
            else custom_strategies[0],
        )
        mtd_operation.proceed_mtd()

    if finish_time is not None:
        env.run(until=(finish_time - start_time))
    else:
        env.run(until=end_event)

    evaluation = Evaluation(network=time_network, adversary=adversary)
    return evaluation
