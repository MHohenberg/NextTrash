#!/usr/bin/python3

from ics import Calendar, Event
from datetime import date
import arrow

print("Die nächsten Abfuhrtermine für STANDORT\n");

present = arrow.utcnow();
earliest_betty = present.shift(years = 1);
earliest_restmuell = present.shift(years = 1);
earliest_grueneTonneAltpapier = present.shift(years = 1);
earliest_grueneTonneLeichtverpackungen = present.shift(years = 1);

icsfile = open("allestrassenniedernhall.ics")
icscontents = icsfile.read()
icsfile.close()

c = Calendar(icscontents)

for e in c.events:
	if (e.begin > arrow.utcnow()):
		if ("BETty" in e.name):
			if (e.begin < earliest_betty):
				earliest_Betty = e.begin;
		if ("Restmüll" in e.name):
			if (e.begin < earliest_restmuell):
				earliest_restmuell = e.begin;
		if ("Altpapier" in e.name):
			if (e.begin < earliest_grueneTonneAltpapier):
				earliest_grueneTonneAltpapier = e.begin;
		if ("Leichtverpackung" in e.name):
			if (e.begin < earliest_grueneTonneLeichtverpackungen):
				earliest_grueneTonneLeichtverpackungen = e.begin;

print ("BETty                {}".format(earliest_betty.humanize()));
print ("Restmüll             {}".format(earliest_restmuell.humanize()));
print ("Altpapier            {}".format(earliest_grueneTonneAltpapier.humanize()));
print ("Leichtverpackungen   {}".format(earliest_grueneTonneLeichtverpackungen.humanize()));

