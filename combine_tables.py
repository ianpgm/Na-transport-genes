translocating_ion_table = open("translocating_ion_table.tdt")

translocating_ion_dict = dict()

for line in translocating_ion_table:
	translocating_ion_dict[line.split("\t")[0]] = line.split("\t")[1].strip("\n")
	
Na_genes_table = open("Na-genes-table.tdt")

output_file = open("Na-genes-table-ATPion.tdt", "w")

for line in Na_genes_table:
	if line.startswith("Genome"):
		output_file.write(line.strip("\n") + "ATPion\n")
		continue
	species = line.split("\t")[0]
	if species in translocating_ion_dict.keys():
		output_file.write(line.strip("\n") + translocating_ion_dict[species] + "\n")
	else:
		output_file.write(line.strip("\n") + "0\n")