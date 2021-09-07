# qubo and ising problems from example is the same partition of variables (same problem)
# optimal solutions in both parts into {A, K} and {B, C}
# but min ebergy differs due to constraints in problem formulations

# within bqm model in ocean, can use offset feature to add in constant to get
# consistent energy values for optimal solutions between both programs


# uses 'EmbeddingComposite' from 'DWaveSampler' to determine best placement of problem onto hardware
# uses dimod library, specifically importing 'BinaryQuadraticModel', both QUBO and ISING bqms

# Optimal QUBO Solutions:
# - A = 1, B = 0, C = 0, K = 1; Energy: 0.0
# - A = 0, B = 1, C = 1, K = 0; Energy: 0.0

# Optimal Ising Solutions:
# - A = +1, B = -1, C = -1, K = +1; Energy: 0.0
# - A = -1, B = +1, C = +1, K = -1; Energy: 0.0

from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

Q = {('B','B'): 1,
    ('K','K'): 1,
    ('A','C'): 2,
    ('A','K'): -2,
    ('B','C'): -2}

bqm = BinaryQuadraticModel.from_qubo(Q, offset=1) # OFFSET here: 
# offset vs energy levels: (e = o-1)
# 2 = 1
# 1 = 0
# 0 = -1

sampler = EmbeddingComposite(DWaveSampler())

# qubo
sampleset = sampler.sample(bqm,
                           num_reads = 10,
                           label='Example - Simple Ocean Programs: Offsets')
print("QUBO samples:")
print(sampleset)

# ising - i guess there are different ways to conver to ising (bqm.change_vartype('SPIN'))
bqm.change_vartype('SPIN')
sampleset = sampler.sample(bqm,
                           num_reads = 10,
                           label='Example - Simple Ocean Programs: Offsets')
print("\nIsing samples:")
print(sampleset)

# QUBO samples:
#    A  B  C  K energy num_oc. chain_.
# 0  1  0  0  1    0.0      10     0.0
# ['BINARY', 1 rows, 10 samples, 4 variables]
# Ising samples:
#    A  B  C  K energy num_oc. chain_.
# 0 -1 +1 +1 -1    0.0       7     0.0
# 1 +1 -1 -1 +1    0.0       3     0.0
