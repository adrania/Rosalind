# Libraries
import Bio
from Bio import pairwise2
from Bio.Seq import Seq
from numpy import zeros

###### EDIT DISTANCE #######
'''Algorithm that allows the edit distance between two sequences, entered by keyboard or selected by default.'''
'''A matrix with the length of the sequences is generated to calculate the minimum value of the edit distance.'''

# Main program:
print('Algorithm to determine the edit distance between two sequences.')
ans = input('Do you want to write the sequences? (y/n): ')
if ans == 'y':
    seq1 = Seq(input('\tType the first sequence: '))
    seq2 = Seq(input('\tType the second sequence: '))
elif ans == 'n':
    seq1 = Seq('PLEASANTLY')
    seq2 = Seq('MEANLY')

matrix = zeros((len(seq1)+1, len(seq2)+1), dtype = int) # Set the matrix with (len(seq1) + 1) rows and (len(seq2 + 1) columns.
for i in range(1, len(seq1)+1): # The position of each letter of the sequences is filled in with whole numbers.
	matrix[i][0] = i
for i in range(1, len(seq2)+1):
	matrix[0][i] = i

for i in range(1, len(seq1)+1): # Complete the matrix according to Levenshtein
	for j in range(1, len(seq2)+1):
		if seq1[i-1] == seq2[j-1]:
			matrix[i][j] = matrix[i-1][j-1]
		else:
			matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+1)

# Results:
print('\n\t{0}\n\t{1}\n\nThe edit distance for these sequences is {2} modifications.'.format(seq1, seq2, matrix[len(seq1)][len(seq2)]))
