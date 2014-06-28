#!/usr/bin/python
import urllib
import csv
import sys

"""
Author: Alvaro
Date: July 26, 2012
Site: https://github.com/LagrangianPoint
"""

## http://stackoverflow.com/questions/1726402/in-python-how-do-i-use-urllib-to-see-if-a-website-is-404-or-200

print " * * * This program checks if column A of a CSV gets redirected to column B* * *"

# Choosing file to read.
if len(sys.argv) == 1:
	strFile = raw_input("What is the input file name? : ")
else:
	strFile = sys.argv[1]

# Reading data
listData = []
with open(strFile, 'rb') as fh:
	csvreader = csv.reader(fh)
	for row in csvreader:
		listData.append(row)
		
nCorrect = 0
nBroken = 0

# Main loop.		
i = 1
for strFrom, strTo in listData:	
	req = urllib.urlopen(strFrom)
	nStatusCode = req.getcode()
	strRedirectUrl = req.geturl()

	if strRedirectUrl == strTo:
		print " %d) CORRECT" % (i)
		nCorrect += 1
	else:
		if nStatusCode == 200:
			print " %d) CORRECT" % (i)
			nCorrect += 1
		else:
			nBroken += 1
			print " %d) The URL %s  gets redirected to %s , not %s \t[%d status] " % (i, strFrom,strRedirectUrl, strTo,  nStatusCode )
	i += 1
			
print " #### %d broken URLs      %d correct URLs    (%d total) " % (nBroken, nCorrect, len(listData) )


raw_input(" Press enter to exit... ")
