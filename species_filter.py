input_file = open("Na-genes-table.tdt")
output_file = open("Na-genes-table-filtered.tdt", "w")

species_set = set()

for line in input_file:
	species = line.split("_")[0] + "_" + line.split("_")[1]
	if species in species_set:
		continue
	else:
		output_file.write(line)
		species_set.add(species)