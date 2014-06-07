import re
import sys
import os
from collections import OrderedDict

def file_opener(directory, fl):
	"""Opens files and returns their full text."""
	fl_path = os.path.join(directory, fl)
	with open(fl_path, "r+") as f:
		text = f.read()
	return text

def metadata_search(text):
	"""Searches through text and returns metadata info (title, author, translator, illustrator)."""
	title_search = re.compile(r'title:(?P<title>.*)', re.IGNORECASE)
	author_search = re.compile(r'author:(?P<author>.*)', re.IGNORECASE)
	translator_search = re.compile(r'translator:(?P<translator>.*)', re.IGNORECASE)
	illustrator_search = re.compile(r'illustrator:(?P<illustrator>.*)', re.IGNORECASE)

	title = re.search(title_search, text).group('title')
	author = re.search(author_search, text)
	translator = re.search(translator_search, text)
	illustrator = re.search(illustrator_search, text)

	if author:
		author = author.group('author')
	if translator:
		translator = translator.group('translator')
	if illustrator:
		illustrator = illustrator.group('illustrator')
	
	dictionary = OrderedDict([('Title', title), ('Author', author), ('Translator', translator), ('Illustrator', illustrator)])
	return dictionary
	
def keyword_counter(kws, text):
	"""Counts number of user-supplied keywords present in text."""
	searches = {}
	for kw in kws:
		searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
	return len(re.findall(searches[kw], text))

def print_info(directory, kws):
	"""Print metadata info and keyword counts."""
	for fl in os.listdir(directory):
		if fl.endswith('.txt'):
			print "Here's the info for file {}:".format(fl)
			text = file_opener(directory, fl)
			metadata_info = metadata_search(text)
			for i in metadata_info:
				print "{0}: {1}".format(i, metadata_info[i])
			for kw in kws:
				print "The word {0} appears {1} times.".format(kw, keyword_counter(kw, text))
		print "*" * 25

def main():
	directory = sys.argv[1]
	kws = sys.argv[2:]
	print_info(directory, kws)

if __name__ == '__main__':
	main()
	
"""change change change"""