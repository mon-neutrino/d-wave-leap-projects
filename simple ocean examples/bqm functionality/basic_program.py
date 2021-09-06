# provides basic ocean program that creates bqm from qubo (can also adapt from ising) problem and runs on dwave qpu
# uses 'EmbeddingComposite' from 'DWaveSampler' to determine best placement of problem onto hardware
# uses dimod library, specifically importing 'BinaryQuadraticModel'

# Optimal Solutions:
# - A = 1, B = 0, C = 0, K = 1; Energy: -1.0
# - A = 0, B = 1, C = 1, K = 0; Energy: -1.0

from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

# define prob as python dictionary and convert to BQM
Q = {('B','B'): 1,
    ('K','K'): 1,
    ('A','C'): 2,
    ('A','K'): -2,
    ('B','C'): -2}

# convert to BQM w 'BinaryQuadraticModel' from dimod
bqm = BinaryQuadraticModel.from_qubo(Q)

# define sampler to use
sampler = EmbeddingComposite(DWaveSampler())

sampleset = sampler.sample(bqm,
                           num_reads = 10,
                           label='Example - Simple Ocean Programs: BQM')

print(sampleset)

# output
#    A  B  C  K energy num_oc. chain_.
# 0  1  0  0  1   -1.0       6     0.0
# 1  0  1  1  0   -1.0       4     0.0
# ['BINARY', 2 rows, 10 samples, 4 variables]