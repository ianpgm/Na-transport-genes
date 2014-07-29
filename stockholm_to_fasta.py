from Bio import SeqIO
import sys

input_file = open(sys.argv[1])
output_file = open(sys.argv[1] + ".fasta", "w")

record_list = list()

for record in SeqIO.parse(input_file, 'stockholm'):
	record_list.append(record)

SeqIO.write(record_list, output_file, 'fasta')