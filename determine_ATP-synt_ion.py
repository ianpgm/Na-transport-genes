from Bio import SeqIO

accession_lookup = open("genomes_ATP-synt_C_accessions_plusdraft.tdt")
accession_dict = dict()
for line in accession_lookup:
	accession_dict[line.split("\t")[0]] = line.split("\t")[1].strip("\n")

aligned_atp_c_sequences = dict()

for record in SeqIO.parse(open("ATP-synt_C-sequences_plusdraftplusIT.aligned.stockholm.fasta.oneline.fasta"), "fasta"):
	aligned_atp_c_sequences["|".join(record.id.split("|")[1:]).split("_")[0]] = record
print(aligned_atp_c_sequences)

output_file = open("translocating_ion_table_plusdrafts.tdt","w")

for genome in accession_dict:
#	try:
	accession = accession_dict[genome]
	aligned_sequence = aligned_atp_c_sequences[accession]
	defining_amino_acid = aligned_sequence[985]
	print(defining_amino_acid)
	if defining_amino_acid in 'STRQ':
		output_file.write(genome + "\t1\n")
	else:
		output_file.write(genome + "\t0\n")
#	except:
		print("error for " + genome)