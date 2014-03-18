
'''******************************************************************
 * Analyse Tweets
 *
 * Graeme Lyon
 * March 2014
 ******************************************************************'''

import string 
import re
from collections import defaultdict
from collections import Counter
import glob
import os
import sys
print(sys.stdout.encoding)

# Words to remove
noise_words_set = {'14','utc','mar','2014rt','the','to','of','a','in','is','and','on','that',
'be','for','with','about','not','at','you','this','from'}


# Find files
path = r"C:\Users\graem_000\Desktop"
os.chdir(path)
print("Processing files...")
for file in glob.glob("*.txt"):

	# Read file
	txt = open("{}\{}".format(path, file),'r', encoding="utf8").read()

	# Remove punctuation
	for punct in string.punctuation:
	    txt = txt.replace(punct,"")

	# Split into words and make lower case
	words = txt.split()
	words = [item.lower() for item in words]

	# Remove unintersting words
	y = [w for w in words if w not in noise_words_set]
	words = y

	# Make a dictionary of words
	D = defaultdict(int)
	for word in words:
	    D[word] += 1

	# Count the most frequent words
	c = Counter(D)
	print(u"%s" % c.most_common(20))

# # Print most common words that are no
# c = Counter([values[1] for values in D.items()])
# for w in c.most_common(59):
# 	u, v = w
# 	if u not in noise_words_set:
# 		print(w),