document_tagger
===============
doc_tagger.py and doc_tagger_final.py have identical functionality: they search through the texts listed below and return metadata information (title, author, translator, and illustrator), as well as keyword counts for keywords supplied by the user at the command line.

The 14 text files are the full texts of classic titles from Project Gutenberg:
<ol>
<li> The Adventures of Sherlock Holmes</li>
<li>Pride and Prejudice</li>
<li>Alice's Adventures in Wonderland</li>
<li>Grimm's Fairy Tales</li>
<li>Double or Nothing</li>
<li>The Divine Comedy</li>
<li>Leaves of Grass</li>
<li>The Prince</li>
<li>Les Miserables</li>
<li>Adventures of Huckleberry Finn</li>
<li>How to Analyze People on Sight Through the Science of Human Analysis: The Five Human Types</li>
<li>Ulysses</li>
<li>The Adventures of Tom Sawyer</li>
<li>Moby Dick</li>
</ol>
TO USE:
Download document_tagger as a zip file. From the command line, navigate to the directory where the zip file is saved and enter: "<file name: doc_tagger.py or doc_tagger_final.py> . <keyword 1> <keyword 2>... <keyword n>"

For example, to search for the keywords "good" and "bad", you would enter from the command line:
doc_tagger_final.py . good bad
