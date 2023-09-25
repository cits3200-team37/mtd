'''Module defines utility functions for graphs'''
from itertools import chain, combinations
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    set_instance = list(iterable)
    return chain.from_iterable(combinations(set_instance, r) for r in range(len(set_instance) + 1))


def remove_element(element, target_list):
    '''Method returns list with element removed'''
    target_list.remove(element)
    return target_list


def degrees(graph):
    """List of degrees for nodes in `G`.

    G: Graph object

    returns: list of int
    """
    return [graph.degree(u) for u in graph]


def all_pairs(nodes):
    """Generates all pairs of nodes."""
    # pylint: disable=invalid-name
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i < j:
                yield u, v


def node_clustering(G, u):
    '''Method calculates clustering statistic'''
    # pylint: disable=invalid-name
    neighbors = G[u]
    k = len(neighbors)
    if k < 2:
        return np.nan

    edges = [G.has_edge(v, w) for v, w in all_pairs(neighbors)]
    return np.mean(edges)


def clustering_coefficient(graph):
    """Average of the local clustering coefficients.

    G: Graph

    returns: float
    """
    cluster = [node_clustering(graph, node) for node in graph]
    return np.nanmean(cluster)


def path_lengths(graph):
    '''Method computes shortest parth length in graph'''
    length_iter = nx.shortest_path_length(graph)
    for source, dist_map in length_iter:
        for dest, dist in dist_map.items():
            if source != dest:
                yield dist


def characteristic_path_length(graph):
    '''###'''
    return np.mean(list(path_lengths(graph)))


def savefig(filename, **options):
    """Save the current figure.

    Keyword arguments are passed along to plt.savefig

    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html

    filename: string
    """
    print("Saving figure to file", filename)
    plt.savefig(filename, **options)


def underride(dic, **options):
    """Add key-value pairs to d only if key is not in d.

    d: dictionary
    options: keyword args to add to d
    """
    for key, val in options.items():
        dic.setdefault(key, val)

    return dic


def legend(**options):
    """Draws a legend only if there is at least one labeled item.

    options are passed to plt.legend()
    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html

    """
    underride(options, loc="best", frameon=False)

    axes = plt.gca()
    handles, labels = axes.get_legend_handles_labels()
    if handles:
        axes.legend(handles, labels, **options)


def decorate(**options):
    """Decorate the current axes.

    Call decorate with keyword arguments like

    decorate(title='Title',
             xlabel='x',
             ylabel='y')

    The keyword arguments can be any of the axis properties

    https://matplotlib.org/api/axes_api.html

    In addition, you can use `legend=False` to suppress the legend.

    And you can use `loc` to indicate the location of the legend
    (the default value is 'best')
    """
    loc = options.pop("loc", "best")
    if options.pop("legend", True):
        legend(loc=loc)

    plt.gca().set(**options)
    plt.tight_layout()
