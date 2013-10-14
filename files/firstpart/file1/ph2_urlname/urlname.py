from nltk.tokenize import *

import nltk

import re

from urllib import urlopen

import csv 

from nltk.corpus import stopwords

#obtain all the url names

f = open('/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/name.csv')

names = f.read()

t = type(names)

#print t


#PROCESSING THE URL NAMES


#tokenizing the string of url names
 
ntoken = nltk.word_tokenize(names)

print ntoken

#extracting capitalized words

capword = RegexpTokenizer('[A-Z]\w+')

caps = capword.tokenize(names)

#print(caps)

#putting them in a file

f= open("urlcaps.csv", "w")

f.write("\n".join(caps))

f.close()


#adding the tagger

from nltk.corpus import treebank

from nltk.tag import DefaultTagger

from nltk.tag.sequential import ClassifierBasedPOSTagger

default = DefaultTagger('NN')

train_sents = treebank.tagged_sents()[:3000]

test_sents = treebank.tagged_sents()[3000:]

tagger = ClassifierBasedPOSTagger(train=train_sents,backoff=default, cutoff_prob = 0.3 )



#implementing it on the url names

ntag = tagger.tag(ntoken)


#extracting all the noun phrases from URL string

nlist = []

for word,tag in ntag:
	if (tag == 'NN'):
	
		value = "%s" % word
		nlist.append(value)
	
	if (tag == 'NNP'):
	
		value = "%s" % word
		nlist.append(value)
		

	if (tag == 'NNS'):
	
		value = "%s" % word
		nlist.append(value)


	if (tag == 'NNPS'):
	
		value = "%s" % word
		nlist.append(value)


#print(nlist)


#Extracting all the named entities

#function for extracting the named entities

def extract_entity_names(t):

    entity_names = []
    
    if hasattr(t, 'node') and t.node:   #t is the object and node = attribute

        if t.node == 'NE':   #attribute is NE
            entity_names.append(' '.join([child[0] for child in t]))

        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names



#implementing the module of ne

sentences = nltk.sent_tokenize(names)

tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]


tagged_sentences = [tagger.tag(sentence) for sentence in tokenized_sentences]


chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)

#each chunk is a subtree

for sent in chunked_sentences:
    sent.draw()



entity_names = []


for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    
    entity_names.extend(extract_entity_names(tree))
    
    
# Print unique entity names

en_unique = set(entity_names)

print en_unique

#putting these named entities in a file

f = open("ne.csv", "w") #contains ne from the url names
     
f.write("\n".join(en_unique))    

f.close()


#putting all the noun phrases in a file

f = open("noun_all.csv", "w") #contains nouns from the url names
     
f.write("\n".join(nlist))    

f.close()


#forming a set of the url names


#lowercase all the words

lurl = [w.lower() for w in ntoken]

#print(lurl)           #all lowercase words


#remove all repetitions

uvocab = sorted(set(lurl))

#print(uvocab)


#removing stopwords

ufilter = uvocab[:]   #copying the list uvocab to ufilter


for word in ufilter:
	if word in stopwords.words('english'):
		ufilter.remove(word)		

#print(ufilter)

    























