from pegasus_graph import P16, P6
import minorminer.layout as mml, dwave_networkx as dnx, networkx as nx

import matplotlib
try:
    import matplotlib.pyplot as plt
    import matplotlib.colors as mpl_color
except ImportError:
    matplotlib.use("agg")
    import matplotlib.pyplot as plt
    import matplotlib.colors as mpl_color


# Draw a small P6 graph
n = 200
C = nx.random_regular_graph(3, n)

# more info on mml.find_embedding: https://docs.ocean.dwavesys.com/en/latest/docs_minorminer/source/reference/layout_embedding.html#minorminer.layout.find_embedding
# useful when underlying data of source graph is SPATIAL
# and for embedding graphs with nodes of low degree (ie. cubic graph)
emb, (layout_C, layout_P) = mml.find_embedding(C, P6, random_seed=1,
                                                    return_layouts=True,
                                                    threads=3)

plt.figure(figsize=(20, 20))

nx.draw(C)

plt.savefig("simple ocean examples/pegasus embedding video/generated images/sparse_graph.png")
plt.close()

plt.figure(figsize=(20, 20))
dnx.draw_pegasus_embedding(P6, emb, C)
plt.savefig("simple ocean examples/pegasus embedding video/generated images/sparse_embedded.png")
plt.close()


# Draw a large P16 graph (this will take a while!)
if False: # note sure why False

    n = 850
    C = nx.random_regular_graph(3, n)

    emb, (layout_C, layout_P) = mml.find_embedding(C, P16, random_seed=2,
                                                    return_layouts=True, 
                                                    layout=(None, None),
                                                    threads=3, 
                                                    verbose=2, 
                                                    interactive=True, 
                                                    tries=30, 
                                                    max_no_improvement=10000, 
                                                    timeout=10000000)

    plt.figure(figsize=(20, 20))

    nx.draw(C)

    plt.savefig("simple ocean examples/pegasus embedding video/generated images/sparse_graph_big.png")
    plt.close()

    plt.figure(figsize=(20, 20))
    dnx.draw_pegasus_embedding(P16, emb, C)
    plt.savefig("simple ocean examples/pegasus embedding video/generated images/sparse_embedded_big.png")
    plt.close()

    # this double_plot part comes from `double_plot`
    from double_plot import double_plot
    double_plot(C, P16, emb, 'simple ocean examples/pegasus embedding video/generated images/sparse_doubleplot2.png',
                    [{'node_size': 70, 'pos': layout_C},
                    {'node_size': 30}])
