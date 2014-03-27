
'''******************************************************************
 * Analyse Tweets
 *
 * Graeme Lyon
 * March 2014
 ******************************************************************'''

'''FUNCTIONS'''
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


'''MAIN'''
import string 
from collections import defaultdict
from collections import Counter
import glob
import os
import re


# Words to remove
noise_words_set = {'01','02','03','04','05','06','07','08','09','10',
'11','12','13','14','15','16','17','18','19','20',
'21','22','23','24','25','26','27','28','29','30','31',
'utc','mar','2014rt','the','to','of','a','in','is','and','on','that',
'be','for','with','about','not','at','you','this','from','【✔】',' 👍 ','…','é','è','í','í','❞','💙','❝❞'}

# Find file_dict
path = r"C:\Users\graem_000\Desktop\Tweet Logs"
os.chdir(path)

file_dict = dict()

for file in glob.glob("*.txt"):

	print(file)

	# Read file
	txt = open("{}\{}".format(path, file),'r', encoding="utf8").read()

	# Remove non alphanumeric charcters
	new = ''
	# pattern = re.compile('[^a-zA-Z\d\s:]')
	pattern = re.compile('[^a-zA-Z:]')

	for group in chunker(txt, 4096):
		group = pattern.sub(' ', group)
		new = new + group
	txt = new

	# Split into words and make lower case
	words = [item.lower() for item in txt.split()]

	# Remove unintersting words
	words = [w for w in words if w not in noise_words_set]

	# Make a dictionary of words
	word_count = Counter(words)
	file_dict[file] = word_count

	for key, value in file_dict[file].items():
		if (value > 50):
			print(key, value)
	print('\n')