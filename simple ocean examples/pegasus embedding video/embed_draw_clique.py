from pegasus_graph import P16 # import stuff from other files
import networkx as nx, dwave_networkx as dnx
from minorminer import busclique
# minorminer is heuristic tool for minor embedding
# https://docs.ocean.dwavesys.com/en/latest/docs_minorminer/source/sdk_index.html

import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.use("agg") # extra technical stuff ig
    import matplotlib.pyplot as plt

# caching is for when multiple or biclique embeddings need to be computed for single chimera or pegasus graph
clique_cache = busclique.busgraph_cache(P16)
clique_embedding = clique_cache.largest_clique()

K = nx.complete_graph(len(clique_embedding))

# P16 is G : NetworkX graph. A Pegasus graph or a subgraph of a Pegasus graph, as produced by the :func:`dwave_networkx.pegasus_graph` function.
# embeds `clique_embedding` onto P16?
# not too sure what K is for
dnx.draw_pegasus_embedding(P16, clique_embedding, K)
