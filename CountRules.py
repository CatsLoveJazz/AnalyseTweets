import re

words_to_ignore = []
things_to_strip = ["|start|","|end|",".",",","?",")","(","\"",":",";","'s","|","'","=","#"]
words_min_size = 4

#------------------------------------------------------------------------------
def CountWords(text):
	words = text.lower().split()
	wordcount = {}
	for word in words:
		for thing in things_to_strip:
			if thing in word:
				word = word.translate(None, ''.join(things_to_strip))
		if word not in words_to_ignore and len(word) >= words_min_size:
			if word in wordcount:
				wordcount[word] += 1
			else:
				wordcount[word] = 1
	return wordcount


#------------------------------------------------------------------------------
def CountWordOccurance(wordcount, key_list):
	count = 0;
	for key in key_list:
		if key in wordcount:
			count = wordcount[key]
		return count
