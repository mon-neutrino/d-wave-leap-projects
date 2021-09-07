# looks at how cliques (or complete graphs) can be embedded on the Pegasus topology. 
# to run this program, type `python clique_embedding.py N`, where N is a pos int. 
# program will attempt to embed a clique of size N onto a full P16 (the Pegasus topology at the scale of the Advantage chip).

# sys module: DAMN so this lets user type in an argument with the file as they run file in terminal.
# hence why we can type `python clique_embedding.py N` and it will just automatically do it
# more info: https://www.tutorialsteacher.com/python/sys-module
import sys

import networkx as nx
import dwave_networkx as dnx
from minorminer import busclique
from dwave.system.samplers import DWaveSampler

import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.use("agg")   # not sure what this is
    import matplotlib.pyplot as plt

N = int(sys.argv[1])   # uses index [1] which is the N we input. [0] would be filename
G = nx.complete_graph(N)    # creates K_N graph

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))

# Draw the QUBO as a networkx graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, font_size=10, node_size=100, node_color='cyan', ax=axes[0])

# Embed the graph on Chimera
# note '.edgelist', 'dnx.chimera_graph'
dwave_sampler_chimera = DWaveSampler(solver={'topology__type': 'chimera'})
chimera_edges = dwave_sampler_chimera.edgelist
chimera_graph = dnx.chimera_graph(16, edge_list=chimera_edges)
clique_embedding_chimera = busclique.find_clique_embedding(N, chimera_graph)

# Draw the graph embedded on Chimera
dnx.draw_chimera_embedding(chimera_graph, clique_embedding_chimera, embedded_graph=G, unused_color=None, ax=axes[1])

# Embed the graph on Pegasus
dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
pegasus_edges = dwave_sampler_pegasus.edgelist
pegasus_graph = dnx.pegasus_graph(16, edge_list=pegasus_edges)
clique_embedding_pegasus = busclique.find_clique_embedding(N, pegasus_graph)
# identical structure to the chimera section (lines 33-36)

# Draw the graph embedded on Pegasus
dnx.draw_pegasus_embedding(pegasus_graph, clique_embedding_pegasus, embedded_graph=G, unused_color=None, ax=axes[2])
plt.savefig('clique_embedding')

# output: 'clique_embedding.py'