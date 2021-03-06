# Libraries
import Bio
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio.SubsMat import MatrixInfo as matlist

###### GLOBAL ALIGNMENT PROBLEM (BA5E) #######
''Algorithm that allows to perform a global alignment between two sequences, either entered by keyboard or selected by default.''
''Several alignment results are displayed for the sequences. The matrix used for the alignment is Blosum64.''

# Main program:
print('Global alignment algorithm')
ans = input('Do you want to write the sequences? (y/n): ')
if ans == 'y':
    seq1 = Seq(input('\tWrite the first sequence: '))
    seq2 = Seq(input('\tWrite the second sequence: '))
elif ans == 'n':
    seq1 = Seq('PLEASANTLY')
    seq2 = Seq('MEANLY')

matrix_blosum = matlist.blosum62
alig = pairwise2.align.globalds(seq1, seq2, matrix_blosum, -5, -5) # Same penalty (sigma = 5)

# Results 
print('\nThe results of the global alignment are as follows: \n')
for a in alig:
    print(format_alignment(*alig[0])) 