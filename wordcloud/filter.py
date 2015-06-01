#!/usr/bin/python

from collections import Counter

badWords = ['dag', 'Dara'];

# Open a file
allWordsFile = open("words.txt", "r")
allWords = [word for line in allWordsFile for word in line.split()];

print "All words : ",allWords;

# Close opend file
allWordsFile.close()


c = Counter(allWords)
for word, count in c.most_common():
	print word, count



for badWord in badWords:
	allWords.remove(badWord);

print "Filtered words : ", allWords;
