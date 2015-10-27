from Bio import ExPASy, SwissProt
from Bio.SwissProt import KeyWList

#test ID: Q5SLP9
#get GO-Biological process info
#DNA recombination
#DNA repair
#DNA replication

handle = ExPASy.get_sprot_raw('Q9HAV7') #you can give several IDs separated by commas
record = SwissProt.read(handle)

for i in record.cross_references:
    if i[0] == 'GO' and i[2].startswith('P'):
        print i[2].replace('P:','')
    else:
        continue
