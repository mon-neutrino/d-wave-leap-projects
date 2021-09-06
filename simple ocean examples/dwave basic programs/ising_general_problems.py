# basic ocean program that runs ising version of qubo problem on d-wave qpu
# this specific example uses 'EmbeddingComposite' from 'DWaveSampler' to determine best placement of problem onto hardware

# Optimal Solutions:
# - A = +1, B = -1, C = -1, K = +1; Energy: -1.5
# - A = -1, B = +1, C = +1, K = -1; Energy: -1.5

from dwave.system import EmbeddingComposite, DWaveSampler

# define problem as two python dictionaries:
# h = linear, j = quadratic

h = {}
j = {('A','K'): -0.5,
    ('B','C'): -0.5, 
    ('A','C'): 0.5}

# define sampler used to run problem
# this is basically embed the dwave sampler into the sampler variable 
sampler = EmbeddingComposite(DWaveSampler())

# run problem on sampler
sampleset = sampler.sample_ising(h, j,
                                 num_reads = 10,
                                 label='Example - Simple Ocean Programs: Ising')

print(sampleset)

# output
#    A  B  C  K energy num_oc. chain_.
# 0 +1 -1 -1 +1   -1.5       9     0.0
# 1 -1 +1 +1 -1   -1.5       1     0.0
# ['SPIN', 2 rows, 10 samples, 4 variables]