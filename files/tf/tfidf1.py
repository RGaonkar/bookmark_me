import nltk
import sys, re, math, unicodedata
from nltk.tokenize import *
from nltk.corpus import stopwords
import csv


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
            
    print terms_in_doc   #dict of {word : freq}
          
    #increment global frequency
    
    for(word, freq) in terms_in_doc.items():
        if word in global_term_freq:
            global_term_freq[word] += 1
            
        else:
            global_term_freq[word] = 1
            
            
    global_terms_in_doc[f] = terms_in_doc    #this is dict having {f : terms_in_doc}
    
    
    print global_terms_in_doc
    
    
    print('Working through documents :')
  

for f in all_files:

    w = csv.writer(open(f + '_tfidf.csv', 'w'))

    result = []


    #iterate over terms in f, calculate their tf-idf , put in new list

    max_freq = 0;

    for(term, freq) in global_terms_in_doc[f].items():
    
        if freq > max_freq:
        
            max_freq = freq
        

    for(term, freq) in global_terms_in_doc[f].items():
    
        idf = math.log(float(1+num_docs) / float(1 + global_term_freq[term]))
        
        tfidf = float(freq) / float(max_freq) * float(idf)
        
        result.append([tfidf, term])
    
    
    result = sorted(result, reverse=True)
    
    
    print result 


#storing the tfidf value in a file

    top_k = -1

    for key, val in result[:top_k]:

        w.writerow([key, val]) 
    
              
            
        
            
            
            
            
        
              
        
    
    
    
    









