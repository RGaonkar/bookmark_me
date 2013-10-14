#extraction of the raw text, title tag, heading tag, urls, url names

from BeautifulSoup import BeautifulSoup

from nltk.tokenize import *

import nltk

import re

from urllib import urlopen

import csv 


url = "http://hbr.org/2013/04/now-is-our-time/ar/1" 
#keeping this along with other urls


#proxies = {'http': 'http://f2010193:bp1708@10.1.9.23:8080'} 


raw = urlopen(url).read()


cleanraw = nltk.clean_html(raw)

#raw.txt contains the raw text
f = open('raw.txt', 'w')   
f.write(cleanraw) 
f.close()


#Split words by all non-alpha characters
words_raw=re.compile(r'[^A-Z^a-z]+').split(cleanraw)
print words_raw 

#removing all the smartquotes

clean = []

for x in words_raw:
    if "quo" not in x:
        clean.append(x) 

#adding the tagger

from nltk.corpus import treebank

from nltk.tag import DefaultTagger

from nltk.tag.sequential import ClassifierBasedPOSTagger

default = DefaultTagger('NN')

train_sents = treebank.tagged_sents()[:3000]

test_sents = treebank.tagged_sents()[3000:]

tagger = ClassifierBasedPOSTagger(train=train_sents,backoff=default, cutoff_prob = 0.3 )


#applying the tagger

rawtag = tagger.tag(clean)

print rawtag

#extracting all the noun phrases from raw string

nlist = []

for word,tag in rawtag:
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





#storing this in a file


f = open('rawtoken.csv', 'w')    #this file will be used for computing document frequencies

f.write("\n".join(clean)) 
f.close()

#lowercase 

lowercase = []

lowercase = [x.lower() for x in clean]


#form a set

wordset = sorted(set(lowercase))


#put this in a file

f = open('raw_new.csv', 'w')
f.write("\n".join(wordset))
f.close()

#extract the title element

soup = BeautifulSoup(raw)

#print(soup.prettify())


titlestr = soup.title.string

#print titlestr

#Split words by all non-alpha characters
words_title = re.compile(r'[^A-Za-z]+').split(titlestr)
#words_title is a list


#removing all the smartquotes

clean_t = []

for x in words_title:
    if "quo" not in x:
        clean_t.append(x) 


#storing this in a file

f = open('titletoken.csv', 'w')
f.write("\n".join(clean_t)) 
f.close()

#extracting the heading element

value1 = [] #empty list to store the values of h1
value2 = [] #empty list to store the values of h2
value3 = [] #empty list to store the values of h3
value4 = [] #empty list to store the values of h4
value5 = [] #empty list to store the values of h5
value6 = [] #empty list to store the values of h6


#for h1

hd1 = soup.findAll('h1')

for item in hd1:
 	hname1 = item.contents[0]
 #	print(hname1)
 	entry = "%s" % (hname1)
 	value1.append(entry)



head1 = " ".join(value1)

#Split words by all non-alpha characters
words_h1 = re.compile(r'[^A-Z^a-z]+').split(head1)
#words_h1 is a list


#removing all the smartquotes

clean_h1 = []

for x in words_h1:
    if "quo" not in x:
        clean_h1.append(x) 

#print clean_h1
#storing this in a file

f = open("heading1.csv", "w")
f.write("\n".join(clean_h1))
f.close()
 
 
#for h2

hd2 = soup.findAll('h2')

for item in hd2:
 	hname2 = item.contents[0]
 #	print(hname2)
 	entry = "%s" % (hname2)
 	value2.append(entry)

head2 = " ".join(value2)

#Split words by all non-alpha characters
words_h2 = re.compile(r'[^A-Z^a-z]+').split(head2)
#words_h2 is a list


#removing all the smartquotes

clean_h2 = []

for x in words_h2:
    if "quo" not in x:
        clean_h2.append(x) 

#print clean_h2

#storing this in a file

f = open("heading2.csv", "w")
f.write("\n".join(clean_h2))
f.close()

	
#for h3

hd3 = soup.findAll('h3')
for item in hd3:
 	hname3 = item.contents[0]
 #	print(hname3)
 	entry = "%s" % (hname3)
 	value3.append(entry)

head3 = " ".join(value3)
	

#Split words by all non-alpha characters
words_h3 = re.compile(r'[^A-Z^a-z]+').split(head3)
#words_h3 is a list


#removing all the smartquotes

clean_h3 = []

for x in words_h3:
    if "quo" not in x:
        clean_h3.append(x) 

#print clean_h3

#storing this in a file

f = open("heading3.csv", "w")
f.write("\n".join(clean_h3))
f.close()

#for h4

hd4 = soup.findAll('h4')
for item in hd4:
 	hname4 = item.contents[0]
# 	print(hname4)
 	entry = "%s" % (hname4)
 	value4.append(entry)
 

head4 = " ".join(value4)
	
#Split words by all non-alpha characters
words_h4 = re.compile(r'[^A-Z^a-z]+').split(head4)
#words_h4 is a list


#removing all the smartquotes

clean_h4 = []

for x in words_h4:
    if "quo" not in x:
        clean_h4.append(x) 


#print clean_h4

#storing this in a file

f = open("heading4.csv", "w")
f.write("\n".join(clean_h4))
f.close()


#for h5

hd5 = soup.findAll('h5')
for item in hd5:
 	hname5 = item.contents[0]
# 	print(hname5)
 	entry = "%s" % (hname5)
 	value5.append(entry)

head5 = " ".join(value5)
	
#Split words by all non-alpha characters
words_h5 = re.compile(r'[^A-Z^a-z]+').split(head5)
#words_h5 is a list


#removing all the smartquotes

clean_h5 = []

for x in words_h5:
    if "quo" not in x:
        clean_h5.append(x) 

#print clean_h5

#storing this in a file

f = open("heading5.csv", "w")
f.write("\n".join(clean_h5))
f.close()


#for h6
hd6 = soup.findAll('h6')
for item in hd6:
 	hname6 = item.contents[0]
 #	print(hname6)
 	entry = "%s" % (hname6)
 	value6.append(entry)

head6 = " ".join(value6)
	
#Split words by all non-alpha characters

words_h6 = re.compile(r'[^A-Z^a-z]+').split(head6)

#words_h6 is a list


#removing all the smartquotes

clean_h6 = []

for x in words_h6:
    if "quo" not in x:
        clean_h6.append(x) 


#print clean_h6

#storing this in a file

f = open("heading6.csv", "w")
f.write("\n".join(clean_h6))
f.close()

#extracting urls and their names

name_list = []

link_list = []

link_list.append(url)   #putting the main url of the page in this list first

for item in soup.findAll('a'):

	if item.has_key("href"):
	
		name = item.text
		
		name_list.append(name)		
				
		href = item["href"]
		
		link_list.append(href)
		
		
namestr = " ".join(name_list)


#Split words by all non-alpha characters
words_uname = re.compile(r'[^A-Z^a-z]+').split(namestr)
#words_h1 is a list


#removing all the smartquotes

clean_unames = []

for x in words_uname:
    if "quo" not in x:
        clean_unames.append(x) 

#print clean_unames


#print link_list

#storing this in a file

f = open("name.csv", "w")
f.write("\n".join(clean_unames))
f.close()



#print clean_unames    #encoding error solved

#Consists of all the links

link = " ".join(link_list)
	

#Split words by all non-alpha characters

words = re.compile(r'[^A-Z^a-z]+').split(link)

 
f= open("link.csv", "w")


f.write("\n".join(words))

f.close()

