import codecs

import nltk

from nltk.tokenize import *

import re

from nltk.corpus import stopwords

import csv 

from nltk.chunk import ne_chunk   #for extracting named entities

f = codecs.open('/media/34227B6E227B3448/projectBooKmarks/mid_sem/file1/phase1/heading3.csv', 'r', 'utf-8-sig')

item = f.read()     #in the form of a string

hd_tokens = nltk.word_tokenize(item)


#extracting capitalized words

capword = RegexpTokenizer('[A-Z]\w+')

caps = capword.tokenize(item)

print(caps)

#putting them in a file

f= open("caps.csv", "w")

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


#tagger.evaluate(test_sents)


#applying the tagger

htag = tagger.tag(hd_tokens)

print(htag)


#extracting all the noun phrases from raw string

nlist = []

for word,tag in htag:
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
		


print(nlist)


#putting all the noun phrases in a file

f = open("noun_all.csv", "w") #contains nouns from the url names
     
f.write("\n".join(nlist))    

f.close()

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

sentences = nltk.sent_tokenize(item)

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

print (en_unique)

#putting these named entities in a file

f = open("ne.csv", "w") #contains ne from the h1
     
f.write("\n".join(en_unique))    

f.close()



	
#lowercase all the words

lh = [w.lower() for w in hd_tokens]

print(lh)   #all lowercase words


#remove all repetitions

hvocab = sorted(set(lh))

print(hvocab)

#removing stopwords

hfilter = hvocab[:]

for word in hfilter:
	if word in stopwords.words('english'):
		hfilter.remove(word)		


