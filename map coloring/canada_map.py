# https://github.com/dwave-examples/map-coloring/blob/master/map_coloring.py

import dwavebinarycsp
from hybrid.reference.kerberos import KerberosSampler
# kerberos hybrid sample runs 3 sampling branches in parallel
# in each iteration, best results from tabu search and simualted annealing are combined with best results from QPU sample a subproblem
# https://docs.ocean.dwavesys.com/en/latest/docs_hybrid/reference/reference.html?highlight=kerberos#module-hybrid.reference.kerberos

# from utilities import visualize_map


# create class of province
class Province:
    def __init__(self, name):
        self.name = name
        self.red = name + "_r"
        self.green = name + "_g"
        self.blue = name + "_b"
        self.yellow = name + "_y"


# set up province
bc = Province("bc")   # British Columbia
ab = Province("ab")   # Alberta
sk = Province("sk")   # Saskatchewan
mb = Province("mb")   # Manitoba
on = Province("on")   # Ontario
qc = Province("qc")   # Quebec
nl = Province("nl")   # Newfoundland and Labrador
nb = Province("nb")   # New Brunswick
pe = Province("pe")   # Prince Edward Island
ns = Province("ns")   # Nova Scotia
yt = Province("yt")   # Yukon
nt = Province("nt")   # Northwest Territories
nu = Province("nu")   # Nunavut

# maybe easier way to do ^
# prov_list = ['bc', 'ab', 'sk', 'mb', 'on', 'qc', 'nl', 'nb', 'pe', 'ns', 'yt', 'nt', 'nu']

# for x,y in zip(prov_list, prov_list):
#     globals()[x] = Province(y)

provinces = [bc, ab, sk, mb, on, qc, nl, nb, pe, ns, yt, nt, nu]

print(provinces)