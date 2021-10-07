# https://github.com/dwave-examples/map-coloring/blob/master/map_coloring.py

import dwavebinarycsp
from hybrid.reference.kerberos import KerberosSampler
# kerberos hybrid sample runs 3 sampling branches in parallel
# in each iteration, best results from tabu search and simualted annealing are combined with best results from QPU sample a subproblem
# https://docs.ocean.dwavesys.com/en/latest/docs_hybrid/reference/reference.html?highlight=kerberos#module-hybrid.reference.kerberos

from utilities import visualize_map



