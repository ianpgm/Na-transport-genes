import os

genome_filenames = list()

for line in open("list_of_genomes"):
	genome_filenames.append(line.strip("\n"))

for genome in genome_filenames:
	os.system("hmmscan --tblout hmm_output/" + genome + ".hmm_output 14_sodium_hmms genomes/" + genome)