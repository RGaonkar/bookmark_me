#extraction of the raw text, title tag, heading tag, urls, url names

from BeautifulSoup import BeautifulSoup

from nltk.tokenize import *

import nltk

import re

from urllib import urlopen

import csv 

from nltk.corpus import stopwords


url = "http://hbr.org/2013/04/now-is-our-time/ar/1" 
#keeping this along with other urls


proxies = {'http': 'http://f2010193:bp1708@10.1.9.23:8080'} 

raw = urlopen(url, proxies=proxies).read()

cleanraw = nltk.clean_html(raw)


#raw.txt contains the raw text
f = open('raw.txt', 'w')   
f.write(cleanraw) 
f.close()


#tokenize cleanraw
tok_clean = nltk.word_tokenize(cleanraw)


#removing all the smartquotes

clean = []

for x in tok_clean:
    if "&" not in x:
        clean.append(x) 


#storing this in a file


f = open('rawtoken.csv', 'w')    #this file will be used for computing document frequencies

f.write("\n".join(clean)) 
f.close()



#extract the title element

soup = BeautifulSoup(raw)

titlestr = soup.title.string

#print(titlestr)

title_tokens = nltk.word_tokenize(titlestr)

#eliminating smart quotes from the title tag

clean_title = []

for x in title_tokens:
    if "&" not in x:
        clean_title.append(x) 


#print(title_tokens)

f = open('titletoken.csv', 'w')
f.write("\n".join(clean_title)) 
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

#eliminating smart quotes from h1

clean_h1 = []

for x in value1:
    if "&" not in x:
        clean_h1.append(x) 

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

#eliminating smart quotes from the h2

clean_h2 = []

for x in value2:
    if "&" not in x:
        clean_h2.append(x) 

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

#eliminating smart quotes from h3

clean_h3 = []

for x in value3:
    if "&" not in x:
        clean_h3.append(x) 

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
 
#eliminating smart quotes from h4

clean_h4 = []

for x in value4:
    if "&" not in x:
        clean_h4.append(x) 

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

#eliminating smart quotes from h5

clean_h5 = []

for x in value5:
    if "&" not in x:
        clean_h5.append(x) 

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

#eliminating smart quotes from h5

clean_h6 = []

for x in value6:
    if "&" not in x:
        clean_h6.append(x) 

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
		
		
#namestr = "\t".join(name_list)	

#name = namestr.decode("utf-8")

#name.replace(u"\u2018", "").replace(u"\u2019", "").replace(u"\u201c","").replace(u"\u201d", "")	



#the entire list is exported to urlnames.csv



#convert list to a string


#eliminating smart quotes from url names

clean_unames = []

for x in name_list:
    if "&" not in x:
        clean_unames.append(x) 


namestr = " ".join(clean_unames)


#Split words by all non-alpha characters
words=re.compile(r'[^A-Z^a-z]+').split(namestr)


print words    #encoding error solved



f= open("name.csv", "w")

f.write("\n".join(words))
	
f.close()



#print(namestr)

#ntoken = nltk.word_tokenize(namestr)



#consists of all the links

f= open("link.csv", "w")


f.write("\n".join(link_list))

f.close()

