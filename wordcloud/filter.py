#!/usr/bin/python
# coding=utf-8

from collections import Counter

# forsetningar
# atviksorð
# samtengingar
# upphrópanir
# nafnháttarmerki

badWords = ['er','að','af','aldrei','alltaf','annaðhvort','auk','á','áður','án','ásamt','ávallt','bráðum','bæði','eða','ef','eftir','eigi','ekki','ellegar','en','enda','fram','frá','fyrir','gegn','gegnt','gegnum','handa','heim','heldur','hér','hérna','hingað','hjá','hó','hvar','hve','hvenær','hvernig','hversu','hvert','hví','hvorki','hvort','hæ','inn','í','jú','kringum','lengi','með','meðal','meðan','meðfram','mé','milli','nei','nema','né','niður','nú','og','ó','samkvæmt','sem','stundum','til','um','undan','undir','upp','uss','ú','úr','út','vegna','við','víða','yfir','ýmist','þar','þarna','þá','þegar','æ','ætíð','m.a','t.d','o.fl',' '];

print "";
print "- Les inn skrá (words.txt).";
allWordsFile = open("words.txt", "r")
# skrá splittað niður í orð
allWordsRaw = [word for line in allWordsFile for word in line.split()];
# Close opend file
allWordsFile.close()


print "- Hreinsa drasl af orðunum.";
allWords = [];
for rawWord in allWordsRaw:
	strippedRawWord = rawWord.lower().strip('";:., \t\n\r»,«-()');
	if(len(strippedRawWord)>1):
		allWords.append(strippedRawWord);


print "- Hendi út smáorðum.";
filteredWords = [];
for aWord in allWords:
	if not(aWord in badWords):
		filteredWords.append(aWord);





print "- Tel saman og skrifa í skrá (wordcount.txt).";

outputFile = open("wordcount.txt", "wb")
c = Counter(filteredWords);
for word, count in c.most_common():
	outputFile.write(word+"\t"+str(count)+"\n");
outputFile.close()

print "- Búið!\n";







