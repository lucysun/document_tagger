import sys
import os
import re

directory = sys.argv[1]

searches = {}
for kw in sys.argv[2:]:
    searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

title_search = re.compile(r'(?:title:\s*)(?P<title>((\S*( )?)+)' + 
                          r'((\n(\ )+)(\S*(\ )?)*)*)', 
                          re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

for fl in (os.listdir(directory)):
    if fl.endswith('.txt'):
        fl_path = os.path.join(directory, fl)

        with open(fl_path, 'r') as f:
            text = f.read()
         
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

        print "***" * 25
        print "Here's the info for doc {}:".format(fl)
        print "Title:  {}".format(title)
        print "Author(s): {}".format(author)
        print "Translator(s): {}".format(translator)
        print "Illustrator(s): {}".format(illustrator)
        print "Here's the counts for the keywords you searched for:"
        for search in searches:
            print "\"{0}\": {1}".format(search, len(re.findall(searches[search], text)))