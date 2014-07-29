genome_filenames = list()
for line in open("list_of_genomes"):
	genome_filenames.append(line.strip("\n"))

hmms = ['ATP-synt_C','Ion_trans_2','MNHE','MtrA','NQR2_RnfD_RnfE','NQRA','Na_Ca_ex','Na_H_Exchanger','Na_H_antiport_1','Na_H_antiport_2','NhaB','OAD_beta','Rnf-Nqr','TrkH']
default_output_list = list()


header_line =str('Genome\t')
for hmm in hmms:
	header_line = header_line + hmm + '\t'
	default_output_list.append(0)

output_file = open("Na-genes-table.tdt", "w")
output_file.write(header_line + "\n")

for genome in genome_filenames:
	output_list = list([0]*len(default_output_list))
	output_string = genome + "\t"
	try:
		hmm_results = open("hmm_output/" + genome + ".hmm_output")
	except:
		print("error for " + genome)
#	try:
	for line in hmm_results:
		if line.startswith("#"):
			continue
		else:
			for hmm in enumerate(hmms):
				if line.startswith(hmm[1]):
					output_list[hmm[0]] = 1
	for output in output_list:
		output_string = output_string + str(output) + "\t"
	output_file.write(output_string + "\n")
#	except:
#		print("error for " + genome)