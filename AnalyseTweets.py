
'''******************************************************************
 * Analyse Tweets
 *
 * Graeme Lyon
 * March 2014
 ******************************************************************'''

import string 
import re
from collections import Counter

# Words to remove
noise_words_set = {'utc','2014rt','the','to','of','a','in','is','and','on','that',
'be','for','with','about','not','at','you','this','from'}

# Read file
txt = open(r'C:\Users\graem_000\Desktop\Tweet Logs\log_13__07_03_2014.txt','r', encoding="utf8").read()

# Remove punctuation
for punct in string.punctuation:
    txt = txt.replace(punct,"")

# Split into words and make lower case
words = txt.split()
words = [item.lower() for item in words]

# Print most common words that are no
c=Counter(words)
for w in c.most_common(10):
	u, v = w
	if u not in noise_words_set:
		print(w),