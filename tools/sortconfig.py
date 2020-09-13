#!/usr/bin/python3

import sys

def sort_ini(fname):
	f = open(fname)
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
		sk = sorted(sk)
		for k in sk:
			vals = sections[k]
			vals.sort()
			print(k)
			print('\n'.join(vals))
			print("")

sort_ini(sys.argv[1])
