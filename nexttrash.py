#!/usr/bin/python3

#    Copyright (C) 2020-2021 Martin Hohenberg <me@martinhohenberg.de>
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
import sys
import getopt
import configparser
import arrow
from AbfallTyp import AbfallTyp

configdir = os.path.expanduser('~')+"/.nexttrash"
config = configparser.ConfigParser()
config.read(configdir+"/config.ini")
maxLength = 0

termine = []

icsFile = configdir+"/termine.ics"
reportDate = arrow.utcnow()

# Parameter-check
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["date=","help","icsfile="])
except getopt.GetoptError:
    sys.exit(3)

for opt, arg in opts:
    if opt == '--help':
        print('nexttrash [--date=<date>] [--icsfile=<filename>] [--help]')
        sys.exit()
    if opt == "--icsfile":
        if (os.path.isfile(arg) == False):
            print("No such file "+arg)
            sys.exit(4)
        icsFile=arg
    if opt == '--date':
        try:
            reportDate = arrow.get(arg, 'YYYY-MM-DD')
        except:
            print("Error in date format. Use YYYY-MM-DD")
            sys.exit(5)

#### end Parameter check                                

use_config = config['general']['use_config']

for typdef in config[use_config]['types'].split(','):
        if (len(typdef) > maxLength):
                maxLength = len(typdef)
        termine.append(AbfallTyp(typdef));

present = arrow.utcnow()
icsfile = open(icsFile)
icscontents = icsfile.read()
icsfile.close()

c = Calendar(icscontents)
calendarHasChanged = False

for e in c.events.copy():
    if (e.begin >= reportDate):
        for i in range(0, len(termine)):
            if (termine[i].name in e.name):
                termine[i].neuesDatum(e.begin)
    else:
        calendarHasChanged = True
        c.events.remove(e)

if calendarHasChanged == True:
	with open(icsFile, 'w') as new_ics_file:
		new_ics_file.writelines(c)
		

print("Die nächsten Abfuhrtermine")
print("--------------------------\n")

for i in range(0,len(termine)):
        if (termine[i].everChanged == True):
                print (termine[i].name.ljust(maxLength + 3," ")+termine[i].datum.humanize()+" ("+termine[i].datum.format("MMM-DD")+")")
print("")
