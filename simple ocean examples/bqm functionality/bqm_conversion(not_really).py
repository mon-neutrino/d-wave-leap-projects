# my version - just following same format as basic program but applied for the ising libraries instead
# turns out it doesn't actually involve coversion lol
# actual conversion is at 'qubo_ising_nbm_conversion.py'


# provides basic ocean program that takes bqm from 'basic_problem.py', convert to Ising and runs on dwave qpu
# uses 'EmbeddingComposite' from 'DWaveSampler' to determine best placement of problem onto hardware
# uses dimod library, specifically importing 'BinaryQuadraticModel'

# Optimal Solutions:
# - A = +1, B = -1, C = -1, K = +1; Energy: -1.5
# - A = -1, B = +1, C = +1, K = -1; Energy: -1.5

from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

# define problem as two python dictionaries:
# h = linear, j = quadratic

h = {}
j = {('A','K'): -0.5,
    ('B','C'): -0.5, 
    ('A','C'): 0.5}

# convert to BQM w 'BinaryQuadraticModel' from dimod
bqm = BinaryQuadraticModel.from_ising(h,j)

sampler = EmbeddingComposite(DWaveSampler())

sampleset = sampler.sample(bqm,
                           num_reads = 10,
                           label='Example - Simple Ocean Programs: BQM')

print(sampleset)

#    A  B  C  K energy num_oc. chain_.
# 0 +1 -1 -1 +1   -1.5       7     0.0
# 1 -1 +1 +1 -1   -1.5       3     0.0
# ['SPIN', 2 rows, 10 samples, 4 variables]