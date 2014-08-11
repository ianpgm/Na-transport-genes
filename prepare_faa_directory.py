import os

for line in open("all_ncbi_genomes_list"):
	foldername = line.strip("\n")
	os.system("cp all_ncbi_genomes/" + foldername + "/*.faa all_ncbi_genomes/")
	os.system("rm -r all_ncbi_genomes/" + foldername + "/")cd 