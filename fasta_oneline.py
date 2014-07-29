import sys
from Bio import SeqIO

output = open(sys.argv[1] + ".oneline.fasta", "w")

for record in SeqIO.parse(open(sys.argv[1]), "fasta"):
	output.write(">" + record.description + "\n" + str(record.seq) + "\n")