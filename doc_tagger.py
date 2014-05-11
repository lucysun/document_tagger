import re
import os
import sys

searches = {}
for kw in sys.argv[2:]:
	searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
	
directory = sys.argv[1]
documents = []
for fl in os.listdir(directory):
	if fl.endswith('txt'):
		fl_path = os.path.join(directory, fl)
		with open(fl_path, "r+") as f:
			text = f.read()
			
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
		
			print "Here's the info for file {}:".format(fl)
			print "Title: {}".format(title)
			print "Author: {}".format(author)
			print "Translator: {}".format(translator)
			print "Illustrator: {}".format(illustrator)
			print "Here are the counts for the keywords you searched for:"
			for kw in searches:
				number = len(re.findall(searches[kw], text))
				print "The word {0} appears {1} times.".format(kw, number)
			print "*" * 25
	
