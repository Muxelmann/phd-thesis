#!/usr/bin/python
import os


def scan_dir(d):
	"""Scans directory `d` for tex files and returns paths"""
	files = os.listdir(d)
	all_files = []
	for f in files:
		if os.path.isdir(d+f):
			# Is a directory, rescan...
			all_files += scan_dir(d+f+'/')
		elif len(f) > 4 and f[-4:] == '.tex':
			all_files.append(d+f)
	return all_files

def fix_nomenclatures(p):
	"""Tex file in path `p` are opened and nomenclature is fixed"""
	f = open(p, 'r')
	content = f.read()
	f.close()



	f = file(p+'.tmp', 'w')
	f.write(content)
	f.close()

	os.rename(p+'.tmp', p)
	print('Finished: {}'.format(p))

base_path = '/Users/maxi/Documents/Reading Uni [PG]/Documents/Thesis (Built Environment)/'

all_files = scan_dir(base_path)
for p in all_files:
	fix_nomenclatures(p)
