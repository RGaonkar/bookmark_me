#analyzing the title tag

from nltk.tokenize import *
import nltk
import re
import csv 
from nltk.corpus import stopwords
from nltk.chunk import ne_chunk   #for extracting named entities

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/file1/phase1/titletoken.csv")

title = f.read()

print (title)

t = type(title)

print(t)

#tokenizing

ttoken = nltk.word_tokenize(title)

#extracting capitalized words

capword = RegexpTokenizer('[A-Z]\w+')

caps = capword.tokenize(title)

print(caps)

#putting them in a file
f= open("caps.csv", "w")

f.write("\n".join(caps))

f.close()


#adding the tagger

import nltk

from nltk.corpus import treebank

from nltk.tag import DefaultTagger

from nltk.tag.sequential import ClassifierBasedPOSTagger

default = DefaultTagger('NN')

train_sents = treebank.tagged_sents()[:3000]

test_sents = treebank.tagged_sents()[3000:]

tagger = ClassifierBasedPOSTagger(train=train_sents,backoff=default, cutoff_prob = 0.3 )


tagger.evaluate(test_sents)

#token = nltk.word_tokenize(title)  #title string tokenized

#removing all the punctuation  marks

#punctuation = re.compile(r'[-.?,":;()`~!@#$%^*()_=+{}]')

#tword = [punctuation.sub("", word) for word in token]

#print(tword) #without punctuation

#removing all the MS smart quotes

#smart_quotes = re.compile(r'[\x80-\x9f]')

#words = [smart_quotes.sub("", i) for i in tword]

#print(words) #without the smart quotes



titletag = tagger.tag(ttoken)   #tagging the list

print(titletag)


#extracting all the noun phrases from title string

nlist = []

for word,tag in titletag:
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

sentences = nltk.sent_tokenize(title)

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



#forming a set of the url names


#lowercase all the words

ltitle = [w.lower() for w in ttoken]

#print(lurl)           #all lowercase words


#remove all repetitions

tvocab = sorted(set(ltitle))

#print(uvocab)


#removing stopwords

tfilter = tvocab[:]   


for word in tfilter:
	if word in stopwords.words('english'):
		tfilter.remove(word)		


    


#eliminating the title elements rawtext 

#f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/phase1/rawtoken.csv")

#raw = f.read()

#rtoken = nltk.word_tokenize(raw)

#raw1 = sorted(set(rtoken) - set(token))


#updating the raw text file

#f= open("rawtoken1.csv", "w")   #this will be used for further processing

#f.write("\n".join(raw1))

#f.close()


#raw set from the filter text file

#f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/phase1/rfilter.csv")

#rfilter = f.read()

#f.close()

#rfilter_token = nltk.word_tokenize(rfilter)

#rfilter1 = sorted(set(rfilter_token) - set(filtered_word_list))


#updating the filter file

#f= open("rfilter1.csv", "w")   #this will be used for futher processing

#f.write("\n".join(rfilter1))

#f.close()

 





