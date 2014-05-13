import re
import os
import sys

#Create separate functions to handle the following items:
#Iterating over and opening files
#Compiling user supplied keywords into  regular expressions
#Counting keywords in a document
#Stripping out metadata (author, title, etc.) from Project Gutenberg documents
#A main() function that calls the other functions, supplying them with the necessary user supplied arguments at run time. 

def make_file_path(directory, fl):
"""Makes a file path given the directory and file name."""
	return os.path.join(directory, fl)

def open_file(file_path):
"""Given a file path, opens the file and returns its contents."""
	with open(file_path, "r+") as f:
		return f.read()

def kw_compiler(kws):
"""Given user-supplied keywords, create regular expressions for searching for them."""
	for kw in kws:
		return re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

def print_results(directory, kws):
	for fl in os.pathdir(directory):
		if fl.endswith('.txt'):
			file_path = make_file_path(directory, fl)
			text = open_file(file_path)
			print "Here's the info for file {}.".format(fl)
			
			
			
