import sys
import os
from collections import Counter
import CountRules as cr

#------------------------------------------------------------------------------
def print_html(sortedbyfrequency):
	minWordCount = 100*len(os.listdir(os.getcwd()))
	f = open("GlobalCount.html", "w")
	f.write("<html><head><title>Wordcount.py GlobalCount</title></head><body><table>")
	for word in sortedbyfrequency:
		wc = wordcount[word]
		if wc > minWordCount:
			f.write("<tr><td>%s</td><td>%s</td></tr>" % (word,wc))
	f.write("</table></body></html>")
	f.close()


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
path = r"/Users/glyon/Documents/Code/AnalyseTweets/test"
text = ""
wordcount = {}
print "Parsing %d files..." % (len(os.listdir(path)))

for file in os.listdir(path):

	# Append all the data
	filepath = "{}/{}".format(path, file)
	f = open(filepath,"rU")
	thisfile = ""
	for line in f:
		thisfile += line
	thiswordcount = cr.CountWords(thisfile)
	wordcount = Counter(wordcount) + Counter(thiswordcount)
 
sortedbyfrequency = sorted(wordcount,key=wordcount.get,reverse=True)

 
print_html(sortedbyfrequency)

#EOF