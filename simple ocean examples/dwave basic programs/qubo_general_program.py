# basic ocean program that runs qubo problem on d-wave qpu
# this specific example uses 'EmbeddingComposite' from 'DWaveSampler' to determine best placement of problem onto hardware

# Optimal Solutions:
# - A = 1, B = 0, C = 0, K = 1; Energy: -1.0
# - A = 0, B = 1, C = 1, K = 0; Energy: -1.0

from dwave.system import EmbeddingComposite, DWaveSampler

# define problem as python dictionary:
Q = {('B','B'): 1,
    ('K','K'): 1,
    ('A','C'): 2,
    ('A','K'): -2,
    ('B','C'): -2}

# define sampler used to run problem
# this is basically embed the dwave sampler into the sampler variable 
sampler = EmbeddingComposite(DWaveSampler())

# run problem on sampler
sampleset = sampler.sample_qubo(Q,
                                 num_reads = 10,
                                 label='Example - Simple Ocean Programs: QUBO')

print(sampleset)

# output
#    A  B  C  K energy num_oc. chain_.
# 0  0  1  1  0   -1.0       4     0.0
# 1  1  0  0  1   -1.0       6     0.0
# ['BINARY', 2 rows, 10 samples, 4 variables]