
from nltk.tokenize import *
import nltk
import re
import csv 
from nltk.corpus import stopwords
from nltk.chunk import ne_chunk   #for extracting named entities


f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/phase1/raw.txt")

raw = f.read()

#Split words by all non-alpha characters
raw_words=re.compile(r'[^A-Z^a-z]+').split(raw)

print(raw_words)

#eliminating smart quotes from rawtext

clean_raw = []

for x in raw_words:
    if "quo" not in x:
        clean_raw.append(x) 



#head6 = " ".join(clean_h6)
	
print clean_raw


#putting it in a file
f = open("rawtext.csv", "w")
f.write("\n".join(clean_raw))
f.close()
 



