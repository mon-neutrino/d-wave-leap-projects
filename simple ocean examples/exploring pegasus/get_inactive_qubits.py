# each time a chip is calibrated, small number of qubits may not perform within required specs. 
# these qubits become inactive, and can't be used in your calculations. 
# program will show the # of inactive qubits in the online Advantage system.


import dwave_networkx as dnx
from dwave.system.samplers import DWaveSampler

dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
props_pegasus = dwave_sampler_pegasus.properties

# Get total qubits - should be 24 * N * (N - 1)
total_qubits = props_pegasus['num_qubits']

# Get total number of inactive qubits
# basically same as 'get_avaiable_qubits.py'
total_inactive = [i for i in range(total_qubits) if i not in dwave_sampler_pegasus.nodelist]
print('number of inactive qubits:', len(total_inactive))
print('number of qubits in use (w/ .nodelist): ', len(dwave_sampler_pegasus.nodelist))

# output
# number of inactive qubits: 324
# number of qubits in use (w/ .nodelist): 5436