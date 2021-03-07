# Libraries
from Bio import pairwise2
from math import log
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio.SubsMat import MatrixInfo as matlist

###### ALIGNMENT WITH AFFINE GAP PENALTIES #######
'''Algorithm that allows the alignment of two sequences, entered by keyboard or selected by default, with penalty for openness.'''
'''The matrix used in the algorithm is Blosum62.'''
    
# Main:
print('Alignment algorithm.')
ans = input('Do you want to write the sequences? (y/n): ')

if ans == 'y':
    seq1 = Seq(input('\tType the first sequence: '))
    seq2 = Seq(input('\tType the second sequence: '))
elif ans == 'n':
    seq1 = Seq('PRTEINS')
    seq2 = Seq('PRTWPSEIN')
    
matrix_blosum = matlist.blosum62   
alig = pairwise2.align.globalds(seq1, seq2, matrix_blosum, -11, -1)
  
# Results
print('\nThe results of the global alignment with penalty are as follows: \n')
for a in alig:
    print(format_alignment(*alig[0])) 