from collections import Counter

def printDNACounter(dna_string):
    c = Counter(dna_string)
    print(c.get('A'), c.get('C'), c.get('G'), c.get('T'))
    
with open('rosalind_dna.txt') as f:
    content = f.readlines()
    
dna_string = content[0]
printDNACounter(dna_string)



