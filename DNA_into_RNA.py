import subprocess

def transcribe(dna_string):
    dna_string = dna_string.replace('T', 'U')
    return dna_string


with open('rosalind_rna.txt') as f:
    content = f.readlines()
    
dna_string = content[0]   
rna = transcribe(dna_string)
print(rna)

newfile = open('rna.txt', 'a')
newfile.write(rna)

f.close()
newfile.close()