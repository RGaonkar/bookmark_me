import nltk
import sys, re, math, unicodedata
from nltk.tokenize import *
from nltk.corpus import stopwords



#a list of (word-freq) pairs for each document
global_terms_in_doc = {}

#a list to hold occurences of terms across documents

global_term_freq = {}

num_docs = 0


reader = open('/media/34227B6E227B3448/projectBooKmarks/mid_sem/bookmarks.txt')

all_files = reader.read().splitlines() #will split it at newline character

#all_files is a list of all the documents containing tokenized raw text after removing non-alphabetical characters

num_docs = len(all_files) #no. of docs to be analyzed

print num_docs

for f in all_files:

    #local term frequency map
    terms_in_doc = {}

    doc_words = open(f).read().lower()  #make all the words lowercase
    
    token = nltk.word_tokenize(doc_words)
    
    
    #removing all the stopwords
    
    filterword = token[:]
    
    
    for word in filterword:
        if word in stopwords.words('english'):
            filterword.remove(word)
            
     
    #increment local count
            
    for word in filterword:
        if word in terms_in_doc:
            terms_in_doc[word] +=1
        else:
            terms_in_doc[word] = 1
            
    print terms_in_doc
