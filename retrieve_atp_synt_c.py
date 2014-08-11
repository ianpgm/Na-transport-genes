from Bio import SeqIO

genome_filenames = list()
for line in open("hmm_output_file_list"):
	genome_filenames.append(line.strip("\n"))

found_atp_sequences = list()
ref_table = open("genomes_ATP-synt_C_accessions_plusdraft.tdt", "w")


for genome in genome_filenames:
	try:
		hmm_results = open("hmm_output/" + genome)
	except:
		print("error for " + genome)
	for line in hmm_results:
		if line.startswith("ATP-synt_C"):
			accession = line[32:52].strip(" ")
			ref_table.write(genome + "\t" + accession + "\n")
	try:
		faa_file = open("all_ncbi_genomes/" + genome.strip(".hmm_output"))
		for record in SeqIO.parse(faa_file, "fasta"):
			if record.id.startswith(accession):
				found_atp_sequences.append(record)
	except:
		print("error for " + genome)

SeqIO.write(found_atp_sequences, "ATP-synt_C-sequences_plusdraft.faa", "fasta")

