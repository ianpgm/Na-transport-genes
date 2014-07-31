from ftplib import FTP

ftp = FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()

ftp.cwd('/genomes/Bacteria_DRAFT/')

ls = list()
folders = list()

ftp.retrlines('MLSD', ls.append)

for entry in ls:
	folders.append(entry.split(" ")[1])

#print(folders)

for folder in folders:
	try:
		if folder.startswith('.'):
			continue
		else:
			ftp.cwd('/genomes/Bacteria_DRAFT/' + folder + "/")
			files_long = list()
			gbk_filename = str()
			ftp.retrlines('MLSD', files_long.append)
			for line in files_long:
				if ".gbk.tgz" in line:
					gbk_filename = line.split(" ")[1]
					output_file = open("ncbi_draft_genomes/" + gbk_filename, "w")
					ftp.retrbinary('RETR ' + gbk_filename, output_file.write)
	except:
		print("Error for " + folder)