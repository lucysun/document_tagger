import re
import os
import sys

def make_file_path(directory, fl):
	"""Makes a file path given the directory and file name."""
	return os.path.join(directory, fl)

def open_file(file_path):
	"""Given a file path, opens the file and returns its contents."""
	with open(file_path, "r+") as f:
		return f.read()

title_search = re.compile(r'title:(?P<title>.*)', re.IGNORECASE)
author_search = re.compile(r'author:(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'translator:(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'illustrator:(?P<illustrator>.*)', re.IGNORECASE)
metadata_dict = {'title': title_search, 'author': author_search, 'translator': translator_search, 'illustrator': illustrator_search} 

def metadata_searcher(metadata_dict, text):
	"""Searches for metadata information (title, author, translator, illustrator) and returns results."""
	results = {}
	for m in metadata_dict:
		result = re.search(metadata_dict[m], text)
		if result:
			results[m] = result.group(m)
	return results

def kw_compiler(kws):
	"""Given user-supplied keywords, creates regular expressions for searching for them."""
	result = {kw: re.compile(r'\b' + kw + r'\b', re.IGNORECASE) for kw in kws}
	return result

def kw_counter(kw_searches, text):
	"""For each keyword, counts the number of occurrences in the text."""
	for kw_search in kw_searches:
		return len(re.findall(kw_search, text))

def print_results(directory, kws):
	"""Prints results of metadata and keyword searches for each file."""
import re
import os
import sys

def make_file_path(directory, fl):
	"""Makes a file path given the directory and file name."""
	return os.path.join(directory, fl)

def open_file(file_path):
	"""Given a file path, opens the file and returns its contents."""
	with open(file_path, "r+") as f:
		return f.read()

title_search = re.compile(r'title:(?P<title>.*)', re.IGNORECASE)
author_search = re.compile(r'author:(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'translator:(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'illustrator:(?P<illustrator>.*)', re.IGNORECASE)
metadata_dict = {'title': title_search, 'author': author_search, 'translator': translator_search, 'illustrator': illustrator_search} 

def metadata_searcher(metadata_dict, text):
	"""Searches for metadata information (title, author, translator, illustrator) and returns results."""
	results = {}
	for m in metadata_dict:
		result = re.search(metadata_dict[m], text)
		if result:
			results[m] = result.group(m)
	return results

def kw_compiler(kws):
	"""Given user-supplied keywords, creates regular expressions for searching for them."""
	result = {kw: re.compile(r'\b' + kw + r'\b', re.IGNORECASE) for kw in kws}
	return result

def kw_counter(pattern, text):
	"""For each keyword, counts the number of occurrences in the text."""
	return len(re.findall(pattern, text))

def print_results(directory, kws):
	"""Prints results of metadata and keyword searches for each file."""
	for fl in os.listdir(directory):
		if fl.endswith('.txt'):
			file_path = make_file_path(directory, fl)
			text = open_file(file_path)
			print "Here's the info for file {}:".format(fl)
			metadata_searches = metadata_searcher(metadata_dict, text)
			for m in metadata_searches:
				print "{0}: {1}.".format(m, metadata_searches[m])
			kw_searches = kw_compiler(kws)
			for kw in kw_searches:
				print "The word {0} appears {1} times.".format(kw, kw_counter(kw_searches[kw], text))
		print "*" *25		

def main():
	directory = sys.argv[1]
	kws = sys.argv[2:]
	print_results(directory, kws)
	
if __name__ == '__main__':
	main()
