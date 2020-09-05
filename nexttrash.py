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

from datetime import date
import os
import arrow

print("Die nächsten Abfuhrtermine\n");

present = arrow.utcnow();
earliest_betty = present.shift(years = 1);
earliest_restmuell = present.shift(years = 1);
earliest_grueneTonneAltpapier = present.shift(years = 1);
earliest_grueneTonneLeichtverpackungen = present.shift(years = 1);

icsfile = open(os.path.expanduser('~')+"/.nexttrash/termine.ics")
icscontents = icsfile.read()
icsfile.close()

c = Calendar(icscontents)

for e in c.events:
	if (e.begin > arrow.utcnow()):
		if ("BETty" in e.name):
			if (e.begin < earliest_betty):
				earliest_betty = e.begin;
		if ("Restmüll" in e.name):
			if (e.begin < earliest_restmuell):
				earliest_restmuell = e.begin;
		if ("Altpapier" in e.name):
			if (e.begin < earliest_grueneTonneAltpapier):
				earliest_grueneTonneAltpapier = e.begin;
		if ("Leichtverpackung" in e.name):
			if (e.begin < earliest_grueneTonneLeichtverpackungen):
				earliest_grueneTonneLeichtverpackungen = e.begin;

print ("Altpapier            {}".format(earliest_grueneTonneAltpapier.humanize()));
print ("BETty                {}".format(earliest_betty.humanize()));
print ("Leichtverpackungen   {}".format(earliest_grueneTonneLeichtverpackungen.humanize()));
print ("Restmüll             {}".format(earliest_restmuell.humanize()));

