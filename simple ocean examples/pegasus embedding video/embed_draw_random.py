from pegasus_graph import P6
import networkx as nx, dwave_networkx as dnx, minorminer

import matplotlib
try:
    import matplotlib.pyplot as plt
    import matplotlib.colors as mpl_color
except ImportError: # probably the case since it's online IDE
    matplotlib.use("agg")
    import matplotlib.pyplot as plt
    import matplotlib.colors as mpl_color

nodes = 80
edge_probability = 0.1
G = nx.gnp_random_graph(nodes, edge_probability, seed=0)
nx.draw(G, node_size=3)
plt.savefig('simple ocean examples/pegasus embedding video/generated images/nx_random.png')

emb = minorminer.find_embedding(G, P6, random_seed=1)
dnx.draw_pegasus_embedding(P6, emb, G, node_size=3)
plt.savefig('simple ocean examples/pegasus embedding video/generated images/dnx_random.png')

# ignore plt.savefig ones for now