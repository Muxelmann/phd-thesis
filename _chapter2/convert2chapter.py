import os


def convert_tex(p):
	if p[-4:] == '.tex':
		# Is TeX file
		f = file(p, 'r')
		content = f.read()
		f.close()

		content = content.replace('{sec/', '{_chapter2/sec/')
		content = content.replace('{fig/', '{_chapter2/fig/')
		content = content.replace('{equ/', '{_chapter2/equ/')
		content = content.replace('{tab/', '{_chapter2/tab/')

		f = file(p+'.tmp', 'w')
		f.write(content)
		f.close()

		os.rename(p+'.tmp', p)
		print('Finished: {}'.format(p))

def scan_dir(d):
	files = os.listdir(d)
	for f in files:
		if os.path.isdir(d+f):
			# Is a directory, rescan...
			scan_dir(d+f+'/')
		else:
			convert_tex(d+f)

base_path = '/Users/maxi/Documents/Reading Uni [PG]/Documents/Thesis (Built Environment)/_chapter2/'
scan_dir(base_path)
