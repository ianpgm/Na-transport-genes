for line in open("Na-genes-table-ATPion.tdt"):
	if line.split("\t")[15] == "1\n":
		print(line)