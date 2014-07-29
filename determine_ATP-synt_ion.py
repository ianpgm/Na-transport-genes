from Bio import SeqIO

genome_filenames = list()
for line in open("list_of_genomes"):
	genome_filenames.append(line.strip("\n"))

accession_lookup = open("genomes_ATP-synt_C_accessions.tdt")
accession_dict = dict()
for line in accession_lookup:
	accession_dict[line.split("\t")[0]] = line.split("\t")[1].strip("\n")

aligned_atp_c_sequences = dict()

for record in SeqIO.parse(open("ATP-synt_C.plusIT.aligned.stockholm.fasta.oneline.fasta"), "fasta"):
	aligned_atp_c_sequences[record.id] = record

output_file = open("translocating_ion_table.tdt","w")

for genome in genome_filenames:
	try:
		accession = accession_dict[genome]
		aligned_sequence = aligned_atp_c_sequences[accession]
		defining_amino_acid = aligned_sequence[963]
		print(defining_amino_acid)
		if defining_amino_acid in 'STRQ':
			output_file.write(genome + "\t1\n")
		else:
			output_file.write(genome + "\t0\n")
	except:
		print("error for " + genome)