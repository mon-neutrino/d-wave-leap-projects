# express problem as CSP w boolean logic
# google colab: https://cloud.dwavesys.com/learning/user/monica_2esing_2e2023_40gmail_2ecom/notebooks/leap/demos/factoring/01-factoring-overview.ipynb#Formulating-the-Problem-for-a-D-Wave-System 
# slides: https://docs.google.com/presentation/d/1Tu6dQtVZgl6xvaaczFNNqKFSDc3uIL5ysYk8S-ucJ9o/edit#slide=id.gec295630ff_0_152

# dwavebinarycsp is useful for constraints like logic gates
import dwavebinarycsp as dbc
from dwave.system import DWaveSampler
from dwave.system import EmbeddingComposite
from collections import OrderedDict

#print a dictionary of all the solutions
def response_to_dict(sampleset):
    results_dict = OrderedDict()
    for sample, energy in sampleset.data(['sample', 'energy']):
        a, b = to_base_ten(sample)
        if (a, b) not in results_dict:
            results_dict[(a, b)] = round(energy, 2)
            
    return results_dict

#converting to base ten funtion
def to_base_ten(sample):
    a = b = 0
    
    # we know that multiplication_circuit() has created these variables
    a_vars = ['a0', 'a1', 'a2']
    b_vars = ['b0', 'b1', 'b2']
    
    for lbl in reversed(a_vars):
        a = (a << 1) | sample[lbl]
    for lbl in reversed(b_vars):
        b = (b << 1) | sample[lbl] 
        
    return a,b

#convert number to binary
P = 15 

bP = "{:06b}".format(P)    # "{:06b}" formats for 6-bit binary
print(bP)

#create multiplication circuit as constraint sat problem
csp = dbc.factories.multiplication_circuit(3)
print(next(iter(csp.constraints)))

#convert to bqm
# stitch func creates BQM w/ value that increases by at least 'min_classical_gap' for each violated constraint
bqm = dbc.stitch(csp, min_classical_gap=1) 
# print will show each different component in the multiplication circuit
print("BQM has {} variables: \n\t{}".format(len(bqm.variables), list(bqm.variables)))


# run multiplication in reverse - need to fix variables of multiplication circuits BQM to binary digits of P
p_vars = ['p0', 'p1', 'p2', 'p3', 'p4', 'p5']

# Convert P from decimal to binary
fixed_variables = dict(zip(reversed(p_vars), "{:06b}".format(P)))
fixed_variables = {var: int(x) for(var, x) in fixed_variables.items()}

# Fix product variables
for var, value in fixed_variables.items():
    bqm.fix_variable(var, value)
    
print("BQM has {} non-fixed variables: \n\t{}".format(len(bqm.variables), list(bqm.variables)))

# Use a D-Wave system as the sampler
sampler = DWaveSampler() 
embedding_sampler = EmbeddingComposite(sampler)

# where the actual minimization takes place...
sampleset = embedding_sampler.sample(bqm, num_reads=100, label='Notebook - Factoring')
print("Best solution found: \n",sampleset.first.sample)

#convert back to base ten
a, b = to_base_ten(sampleset.first.sample)
print("Given integer P={}, found factors a={} and b={}".format(P, a, b))

results = response_to_dict(sampleset)
print(results)
