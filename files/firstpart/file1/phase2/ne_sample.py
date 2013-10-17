import nltk
import re
import csv 
from nltk.corpus import stopwords
from nltk.chunk import ne_chunk   #for extracting named entities

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

sentences = nltk.sent_tokenize("The name of this institute is University of California , Berkley ")

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
