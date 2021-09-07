# looks at how bicliques (or complete bipartite graphs) can be embedded on the Pegasus topology.

import sys
import numpy as np
import networkx as nx
import dwave_networkx as dnx
from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler

import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

# Form the biclique
# looks significantly diff from clique
N = int(sys.argv[1])
# N = 10 (in case sys arg dont work)
nodes1 = np.arange(N)   # subset#1, list of 0 to N-1
nodes2 = [chr(i + ord('a')) for i in range(N)]  # subset#2 - just equal amt of letters as N
B = nx.Graph()
B.add_nodes_from(nodes1, bipartite=0)   # adding nodes in the diff subsets to bipartites
B.add_nodes_from(nodes2, bipartite=1)
for node1 in nodes1:
    for node2 in nodes2:
        B.add_edge(node1, node2)
        # creates the 'webbing' where every point in bipartite #1 is connected with every node in #2

# equivalent to clique from this point

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))

# Draw the QUBO as a networkx graph
pos = nx.spring_layout(B)
nx.draw_networkx(B, pos=pos, font_size=10, node_size=100, node_color='cyan', ax=axes[0])

# Embed the graph on Chimera
dwave_sampler_chimera = DWaveSampler(solver={'topology__type': 'chimera'})
chimera_edges = dwave_sampler_chimera.edgelist
chimera_graph = dnx.chimera_graph(16, edge_list=chimera_edges)
embedding_chimera = find_embedding(B, chimera_graph)

dnx.draw_chimera_embedding(chimera_graph, embedding_chimera, embedded_graph=B, unused_color=None, ax=axes[1])

# Embed the graph on Pegasus
dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
pegasus_edges = dwave_sampler_pegasus.edgelist
pegasus_graph = dnx.pegasus_graph(16, edge_list=pegasus_edges)
embedding_pegasus = find_embedding(B, pegasus_graph)

dnx.draw_pegasus_embedding(pegasus_graph, embedding_pegasus, embedded_graph=B, unused_color=None, ax=axes[2])
plt.savefig('biclique_embedding')

