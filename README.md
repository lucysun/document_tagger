document_tagger
===============
doc_tagger.py and doc_tagger_final.py have identical functionality: they search through the texts listed below and return metadata information (title, author, translator, and illustrator), as well as keyword counts for keywords supplied by the user at the command line.

The 14 text files are the full texts of classic titles from Project Gutenberg:
1. The Adventures of Sherlock Holmes
2. Pride and Prejudice
3. Alice's Adventures in Wonderland
4. Grimm's Fairy Tales
5. Double or Nothing
6. The Divine Comedy
7. Leaves of Grass
8. The Prince
9. Les Miserables
10. Adventures of Huckleberry Finn
11. How to Analyze People on Sight Through the Science of Human Analysis: The Five Human Types
12. Ulysses
13. The Adventures of Tom Sawyer
14. Moby Dick

To use:
Download document_tagger as a zip file. From the command line, navigate to the directory where the zip file is saved and enter: "<file name: doc_tagger.py or doc_tagger_final.py> . <keyword 1> <keyword 2>... <keyword n>"

For example, to search for the keywords "good" and "bad", you would enter from the command line:
doc_tagger_final.py . good bad
