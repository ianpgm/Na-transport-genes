import os

faa_files = open("faa_file_list")

added_species = set()

output_file = open("a", "w")

for line in faa_files:
	annotation = open("all_ncbi_genomes/" + line.strip("\n")).readline()
	species_name = annotation.split("[")[1].strip("]\n")
	species_filename = str()
	for c in species_name:
		if c.isalnum():
			species_filename = species_filename + c
		if c == " ":
			species_filename = species_filename + "_"
	if species_filename not in added_species:
		output_file.close()
		output_file = open("all_ncbi_genomes/" + species_filename + ".faa", "w")
		for faa_line in open("all_ncbi_genomes/" + line.strip("\n")):
			output_file.write(faa_line)
		added_species.add(species_filename)
	else:
		for faa_line in open("all_ncbi_genomes/" + line.strip("\n")):
			output_file.write(faa_line)

os.system("rm a")