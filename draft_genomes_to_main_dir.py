import os

for line in open("ncbi_draft_genomes_speciesname_list"):
	if line.endswith(".faa\n"):
		print(line.strip("\n"))
		os.system("cp ncbi_draft_genomes/" + line.strip("\n") + " all_ncbi_genomes/")