# provides info on available qubits that can be programmed in online Advantage system

import dwave_networkx as dnx # dwave x network library for graphs
from dwave.system.samplers import DWaveSampler

dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
props_pegasus = dwave_sampler_pegasus.properties

# Get total qubits - should be 24 * N * (N - 1)
# ... why 24 * N * (N - 1)? 
# ok N(N-1) makes sense (total # of edges in K_N graph), why 24?
total_qubits = props_pegasus['num_qubits']
print('total qubits: ', total_qubits)
# based on result (5760), here N = 16, it's also on line 23
# well it's called Advantage P16 afterall

# Get total number of inactive qubits
# so '.nodelist' is active qubits/nodes
total_inactive = [i for i in range(total_qubits) if i not in dwave_sampler_pegasus.nodelist]
print('inactive qubits: ',len(total_inactive))

# convert known inactive qubit indices to pegasus coordinates
# notice use of dnx
inactive_pegasus_coord = [dnx.pegasus_coordinates(16).linear_to_pegasus(k) for k in total_inactive]
print('list of inactive qubits (coord)', inactive_pegasus_coord)

# w/ coordinates=True, we only get fabric qubits
# i'm assuming fabric qubits is the map of available qubits "fabric"
# since it's all nodes in pegasus_graph.nodes, but only if node isn't in 'inactive_pegasus_coord'
pegasus_graph = dnx.pegasus_graph(16, coordinates=True)
active_fabric = [node for node in pegasus_graph.nodes if node not in inactive_pegasus_coord]
print('active qubits: ', len(active_fabric))


# another way to compute the number of active qubits
# ... well this was much simpler
active_qubits = dwave_sampler_pegasus.solver.num_active_qubits
print('active qubits: ', active_qubits)

# lowkey want to visualize the fabric
# output at 'available qubits output' because list was long