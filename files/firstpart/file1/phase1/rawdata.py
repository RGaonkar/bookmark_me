#pulling the raw data from the urls and eliminating all the punctuation marks and stopwords

from nltk.tokenize import *

import nltk

import re

from urllib import urlopen

import csv 

reader = open('/media/DC1A16731A164AC2/Documents and Settings/Radhika/My Documents/projectBooKmarks/mid_sem/bookmarks.txt')

all_files = reader.read().splitlines() #will split it at newline character

#all_files is a list consisting of all the urls

len_urls = len(all_files)

#gives the number of bookmarked urls

#Run a for loop so that all the text processing is done for all the bookmarked webpages

for line in all_files:
    url = line
    
    #proxies = {'http' : 'http://f2010193:bp1708@10.1.9.23:8080'}
    
    raw = urlopen(url).read()
    
    cleanraw = nltk.clean_html(raw)
    
    #Split words by all non-alpha characters
    words_raw=re.compile(r'[^A-Z^a-z]+').split(cleanraw)
    #words_raw is a list
    
    print type(words_raw)

    #removing all the smartquotes

    print words_raw.strip()
    
    '''
    clean = []

    for x in words_raw:
        if "quo" not in x:
            clean.append(x) 
       '''     
            




