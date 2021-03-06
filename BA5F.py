# Libraries
import Bio
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio.SubsMat import MatrixInfo as matlist

####### LOCAL ALIGNMENT PROBLEM (BA5F) #######
'''Algorithm that allows a local alignment to be performed between two sequences, entered by keyboard or selected by default.'''
'''The alignment with the best score is shown. The matrix used for the alignment is Pam250.'''

# Main program: 
print('Algorithm for local sequence alignment')
ans = input('Do you want to write the sequences? (y/n): ')
if ans == 'y':
    seq1 = Seq(input('\tWrite the first sequence: '))
    seq2 = Seq(input('\tWrite the second sequence: '))
elif ans == 'n':
    seq1 = Seq('MEANLY')
    seq2 = Seq('PENALTY')

matrix_pam = matlist.pam250    
alig = pairwise2.align.localds(seq1, seq2, matrix_pam, -5, -5) # Same penalty (sigma = 5)

# Results:
print('\nThe results of the local alignment are as follows: \n')
for a in alig:
    print(format_alignment(*alig[0]))