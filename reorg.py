#!/usr/bin/env python

import sys
import json
from pprint import pprint

def sortOnViews(val):
	return val[1]["views"]
	
def sortOnClones(val):
	return val[1]["clones"]

with open(sys.argv[1], "r") as input:
	data = json.load(input)
	
	view_sort = sorted(data.items(), key = sortOnViews, reverse=True)
	clone_sort = sorted(data.items(), key = sortOnClones, reverse=True)
	
	with open("stats.rst", "w") as output:
		output.write("==================================\n")
		output.write("Epics Module Repository Popularity\n")
		output.write("==================================\n")
		
		output.write("\n\n\n")
			
		output.write("Repository Clonings (last 14 days)\n")
		output.write("----------------------------------\n")
		output.write(".. csv-table::\n")
		output.write("   :header: Module, Clones\n\n")
		
		for item in clone_sort:
			output.write("   " + item[0].encode("ascii", "ignore") + ", " + str(item[1]["clones"]) + "\n")

		output.write("\n\n\n")
		
		output.write("Repository Views (last 14 days)\n")
		output.write("-------------------------------\n")
		output.write(".. csv-table::\n")
		output.write("   :header: Module, Views\n\n")
	
		for item in view_sort:
			output.write("   " + item[0].encode("ascii", "ignore") + ", " + str(item[1]["views"]) + "\n")
