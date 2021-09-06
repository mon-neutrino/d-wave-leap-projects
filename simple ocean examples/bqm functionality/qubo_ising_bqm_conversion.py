from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

# Define the problem as a Python dictionary and convert it to a BQM
Q = {('B','B'): 1,
    ('K','K'): 1,
    ('A','C'): 2,
    ('A','K'): -2,
    ('B','C'): -2}

bqm = BinaryQuadraticModel.from_qubo(Q)

# Convert the bqm to an Ising model
ising_model = bqm.to_ising() # cool

sampler = EmbeddingComposite(DWaveSampler())

# so bqm.to_ising() automatically creates the two libraries for linear and qudratic terms for ising
sampleset = sampler.sample_ising(
                h = ising_model[0],
                J = ising_model[1],
                num_reads = 10,
                label='Example - Simple Ocean Programs: Conversion')

print(sampleset)

# output
#    A  B  C  K energy num_oc. chain_.
# 0 -1 +1 +1 -1   -1.5       9     0.0
# 1 +1 -1 -1 +1   -1.5       1     0.0
# ['SPIN', 2 rows, 10 samples, 4 variables]