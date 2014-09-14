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
path = r"/Users/glyon/Documents/Code/AnalyseTweets/TweetData"
text = ""
wordcount = {}
hope_count=[]
fear_count=[]
yes_count=[]
no_count=[]

print "Parsing %d files..." % (len(os.listdir(path)))
n=1;
for file in os.listdir(path):

	# Append all the data
	filepath = "{}/{}".format(path, file)
	f = open(filepath,"rU")
	thisfile = ""
	for line in f:
		thisfile += line
	thiswordcount = cr.CountWords(thisfile)
	#Words
	hope_count.append(cr.CountWordOccurance(thiswordcount, ["hope", "hopes"]))
	fear_count.append(cr.CountWordOccurance(thiswordcount, ["fear", "fears"]))
	yes_count.append(cr.CountWordOccurance(thiswordcount, ["yes"]))
	no_count.append(cr.CountWordOccurance(thiswordcount, ["no"]))


	wordcount = Counter(wordcount) + Counter(thiswordcount)
 
sortedbyfrequency = sorted(wordcount,key=wordcount.get,reverse=True)
 
print_html(sortedbyfrequency)

#Parties
labour_count = (cr.CountWordOccurance(thiswordcount, ["labour"]))
tory_count = (cr.CountWordOccurance(thiswordcount, ["tory","torys","conservative","conservatives"]))
snp_count = (cr.CountWordOccurance(thiswordcount, ["snp"]))
libdem_count = (cr.CountWordOccurance(thiswordcount, ["libdem","libdems"]))
print "labour"
print labour_count
print "tory"
print tory_count
print "snp"
print snp_count
print "libdem"
print libdem_count

#Lists
print "hope"
print hope_count
print "fear"
print fear_count
print "yes"
print yes_count
print "no"
print no_count



#EOF