#!/usr/bin/python
# coding=utf-8

from collections import Counter

# forsetningar
# atviksorð
# samtengingar
# upphrópanir
# nafnháttarmerki

badWords = ['að','af','aldrei','alltaf','annaðhvort','auk','á','áður','án','ásamt','ávallt','bráðum','bæði','eða','ef','eftir','eigi','ekki','ellegar','en','enda','fram','frá','fyrir','gegn','gegnt','gegnum','handa','heim','heldur','hér','hérna','hingað','hjá','hó','hvar','hve','hvenær','hvernig','hversu','hvert','hví','hvorki','hvort','hæ','inn','í','jú','kringum','lengi','með','meðal','meðan','meðfram','mé','milli','nei','nema','né','niður','nú','og','ó','samkvæmt','sem','stundum','til','um','undan','undir','upp','uss','ú','úr','út','vegna','við','víða','yfir','ýmist','þar','þarna','þá','þegar','æ','ætíð'];

print "\n------- Byrja -------\n";

# Open a file
allWordsFile = open("words2.txt", "r")

# skrá splittað niður í orð
allWords = [word for line in allWordsFile for word in line.split()];

# Close opend file
allWordsFile.close()

#print "All words : ",allWords;



#print "All words --------------------------------";



print "allWords ---------------\n",allWords;



#Hendi út smáorðum

filteredWords = [];
for aWord in allWords:
	if not(aWord in badWords):
		filteredWords.append(aWord);


c = Counter(filteredWords);
for word, count in c.most_common():
	print word, count;



print "filteredWords ---------------\n",filteredWords;





