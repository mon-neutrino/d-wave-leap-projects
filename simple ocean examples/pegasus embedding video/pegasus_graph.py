import dwave_networkx as dnx
from matplotlib import pyplot as plt
from random import seed, sample

seed(5640)

# mask_nodes is for: 

# create P16 graph
P16_perfect = dnx.pegasus_graph(16)
mask_nodes = sample(list(P16_perfect), int(.96*len(P16_perfect)))
P16 = P16_perfect.subgraph(mask_nodes).copy()

# create P6 graph
P6_perfect = dnx.pegasus_graph(6)
mask_nodes = sample(list(P6_perfect), int(.96*len(P6_perfect)))
P6 = P6_perfect.subgraph(mask_nodes).copy()

# added myself to experiment with it
# for kwargs in .draw_pegasus, https://networkx.org/documentation/networkx-1.7/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html
dnx.draw_pegasus(P6_perfect, node_color="Yellow", node_size=5, alpha=0.8, width=0.5)
plt.savefig('simple ocean examples/pegasus embedding video/generated images/P6_test.png')