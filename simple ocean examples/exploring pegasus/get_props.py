# prints properties of online system that uses pegasus topology

from dwave.system.samplers import DWaveSampler

dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
props_pegasus = dwave_sampler_pegasus.properties
print('number of qubits: ', props_pegasus['num_qubits'])
num_qubits2 = dwave_sampler_pegasus.solver.num_qubits
print('number of qubits: (again?)',num_qubits2)
print('number of couplers: ', len(props_pegasus['couplers']))

# based on speculation from pg 7 section 2.3 from doc linked in 'README.md', 
# i think h,j are the bias and weights
print('range of linear (bias): ', props_pegasus['h_range'])
print('range of quadratic (weights): ',props_pegasus['j_range'])


# output
# number of qubits:  5760
# number of qubits: (again?) 5760
# number of couplers:  37440
# range of linear (bias):  [-2.0, 2.0]
# range of quadratic (weights):  [-1.0, 1.0]