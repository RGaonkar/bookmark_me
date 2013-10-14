import nltk

from nltk.tokenize import *

import re

from nltk.corpus import stopwords

import csv 

from nltk.chunk import ne_chunk   #for extracting named entities


#extracting the raw data

f = open('/media/34227B6E227B3448/projectBooKmarks/mid_sem/phase8/rawtoken7.csv')

item = f.read()     #in the form of a string

rtoken = nltk.word_tokenize(item)   #tokenizing it

#eliminating all the punctuation marks

punctuation = re.compile(r'[-.?,":;()`~!@#$%^*()_=+{}]')

r = [punctuation.sub("", word) for word in rtoken]

print(r)

#tagger

from nltk.corpus import treebank

from nltk.tag import DefaultTagger

from nltk.tag.sequential import ClassifierBasedPOSTagger


default = DefaultTagger('NN')

train_sents = treebank.tagged_sents()[:3000]

test_sents = treebank.tagged_sents()[3000:]

tagger = ClassifierBasedPOSTagger(train=train_sents,backoff=default, cutoff_prob = 0.3 )


#tagger.evaluate(test_sents)


#applying the tagger

rtag = tagger.tag(r)

print(rtag)

#extracting all the noun phrases from raw string

nlist = []

for word,tag in rtag:
	if (tag == 'NN'):
	
		value = "%s" % word
		nlist.append(value)
	
	if (tag == 'NNP'):
	
		value = "%s" % word
		nlist.append(value)
		
	if (tag == 'NNS'):
	
		value = "%s" % word
		nlist.append(value)


print(nlist)

#named entities

nen = ne_chunk(rtag)

print(nen)

#putting all the noun phrases in a file

f= open("noun_all.csv", "w")

f.write("\n".join(nlist))

f.close()

#extracting capitalized words

capword = RegexpTokenizer('[A-Z]\w+')

caps = capword.tokenize(item)

print(caps)

keys = sorted(set(nlist + caps))

#putting all the candidate keywords in a file

f= open("keys_all.csv", "w")

f.write("\n".join(keys))

f.close()


#lowercase all the words

lr = [w.lower() for w in r]

print(lr)   #all lowercase words


#remove all repetitions

rvocab = sorted(set(lr))

print(rvocab)

#removing stopwords

rfilter = rvocab[:]

for word in rfilter:
	if word in stopwords.words('english'):
		rfilter.remove(word)		

print(rfilter)


#frequency distribution for filtered

fr = nltk.FreqDist(rfilter)


fr_set = fr.keys()

print(fr_set)

fr.plot()

 

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/phase8/rawtoken7.csv")

raw = f.read()

rtok = nltk.word_tokenize(raw)

raw8 = sorted(set(rtok) - set(r))


#updating the raw text file

f= open("rawtoken8.csv", "w")   #this will be used for further processing

f.write("\n".join(raw8))

f.close()


#raw set from the filter text file

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/phase8/rfilter7.csv")

rfil = f.read()

f.close()

rfilter_token = nltk.word_tokenize(rfil)

rfilter8 = sorted(set(rfilter_token) - set(rfilter))  

#updating the raw filter file
 
f= open("rfilter8.csv", "w")   #this will be used for futher processing

f.write("\n".join(rfilter8))

f.close()




	











