import os
from Bio import SeqIO
from Bio.SeqIO import InsdcIO

os.system("mkdir temp")

genomes = list()

for line in open("ncbi_draft_genome_list"):
	genomes.append(line.strip("\n"))

for genome in genomes:
	output_list = list()
	filename = "ncbi_draft_genomes/" + genome
	os.system("tar -zxvf " + filename + " -C temp/")
	os.system("ls -1 temp/ > tmp_gbk_filelist")
	gbk_files = list()
	for line in open("tmp_gbk_filelist"):
		gbk_files.append(line.strip("\n"))
	for gbk_file in gbk_files:
		gbk_handle = open("temp/" + gbk_file)
		contig = SeqIO.read(gbk_handle, "genbank")
		species_name = contig.annotations['source']
		gbk_handle.close()
		gbk_handle = open("temp/" + gbk_file)
		for protein in InsdcIO.GenBankCdsFeatureIterator(gbk_handle):
			output_list.append(protein)
	species_filename = str()
	for c in species_name:
		if c.isalnum():
			species_filename = species_filename + c
		if c == " ":
			species_filename = species_filename + "_"
	output_file = open("ncbi_draft_genomes/" + species_filename + ".faa", "w")
	try:
		SeqIO.write(output_list, output_file, "fasta")
	except:
		print("Error for " + species_filename)
	os.system("rm temp/*.gbk")
	os.system("rm tmp_gbk_filelist")