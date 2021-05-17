#create	a string variable seq
seq='ATGCGACTACGATCGAGGGCC'
# create a variate to store the result
protein=""
# make a dictionary to show which codon matches which protein
codon_dict = {
'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
'TAT':'Y', 'TAC':'Y', 'TAA':'O', 'TAG':'U',
'TGT':'C', 'TGC':'C', 'TGA':'X', 'TGG':'W',
'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Z',
'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'ATT':'I', 'ATC':'I', 'ATA':'J', 'ATG':'M',
'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAT':'N', 'AAC':'B', 'AAA':'K', 'AAG':'K',
'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
#select the DNA triplet and use the dictionary to translate it
for i in range(0,len(seq),3):
    triplet=seq[i:i+3]
    protein+=codon_dict[triplet]
print(protein)

