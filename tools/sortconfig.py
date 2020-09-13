#!/usr/bin/python

import sys

USAGE = 'USAGE:\n\tsortconfig.py file.ini'

def sort_ini(fname):
	f = file(fname)
	lines = f.readlines()
	f.close()
	section = ''
	sections = {}
	for line in lines:
		line = line.strip()
		if line:
			if line.startswith('['):
				section = line
				continue
			if section:
				try:
					sections[section].append(line)
				except KeyError:
					sections[section] = [line, ]
	if sections:
		sk = sections.keys()
		sk.sort()
		for k in sk:
			vals = sections[k]
			vals.sort()
			print k
			print '\n'.join(vals)
			print

else:
	sort_ini(sys.argv[1])
