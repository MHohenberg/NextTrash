#!/usr/bin/python3

#    Copyright (C) 2020  Martin Hohenberg <me@martinhohenberg.de>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ics import Calendar, Event
import os
import configparser
import arrow


class AbfallTyp:
	name = ""
	datum = arrow.utcnow().shift(years = 1)
	everChanged = False

	def __init__(self, name):
		self.name = name

	def neuesDatum(self, datum):
		if datum < self.datum:
			self.everChanged = True
			self.datum = datum


configdir = os.path.expanduser('~')+"/.nexttrash"
config = configparser.ConfigParser()
config.read(configdir+"/config.ini")
maxLength = 0

typDefinitionen = []

use_config = config['general']['use_config']

for typdef in config[use_config]['types'].split(','):
	if (len(typdef) > maxLength):
		maxLength = len(typdef)
	typDefinitionen.append(AbfallTyp(typdef));

present = arrow.utcnow()
icsfile = open(configdir+"/termine.ics")
icscontents = icsfile.read()
icsfile.close()

c = Calendar(icscontents)

for e in c.events:
	if (e.begin > arrow.utcnow()):

		for i in range(0, len(typDefinitionen)-1):
			if (typDefinitionen[i].name in e.name):
				typDefinitionen[i].neuesDatum(e.begin)
print("Die nächsten Abfuhrtermine")
print("--------------------------\n")

for i in range(0,len(typDefinitionen)-1):
	if (typDefinitionen[i].everChanged == True):
		print (typDefinitionen[i].name.ljust(maxLength + 3," ")+typDefinitionen[i].datum.humanize())

