
#determine a word or phrase's weight or relevancy on the webpage . Integrate the results  

import csv 

import nltk

from nltk.tokenize import *



#tfidf = real values
#h6 = 1
#h5 = 0.75
#h4 = 0.5
#h3 = 0.25
#h2 = 0.15
#h1 = 0.10

#rest all are boolean : 1 = present in that tag 0 : absent

#sum all the boolean values including the h tag values and tfidf

#sort the words according to the sum


#instead of having a dict, have a list such that the indices idicate the feature
#0:tfidf
#1:noun
#2:caps
#3:hypertext
#4:title
#5:uname
#6:ne
#7:h1
#8:h2
#9:h3
#10:h4
#11:h5
#12:h6


reader = csv.reader(open('/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/raw_new.csv', 'r'))

result = {}


for row in reader:

    key = row[0]
 
#    if key in result:
        # implement your duplicate row handling here
#        pass
    
    result[key] = row[1:]

#print result


#appending values to the list for each word

#feat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for w in result:
    
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    result[w].append(0)
    

#print result

dic_len = len(result)

#print dic_len

#insert the tfidf values

tfidf = []

f = csv.reader(open('/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/rawtoken.csv_tfidf.csv', 'r'), delimiter='\n')

for row in f:
    tfidf.append(row)

#print(tfidf)


for i1 in xrange(len(tfidf)):

    val = tfidf[i1]

#    print val[0]   #comma separated string

#    val_t = type(val)
    
#    print val_t


    listval = []       #gets updated for each iteration
    
    listval = val[0].split(',')
    
    
#    print listval
    
    
    tfidf[i1] =  listval[:]  #nested list for tfidf
    
#    val_t = type(listval)
    
#    print tfidf[i1]


#print tfidf

for i in xrange(len(tfidf)):

    term = tfidf[i][1]    #ith term
    v = tfidf[i][0]
 
#    print term 
 
    
 #   print v


    if term in result:
        result[term][0] = v
            

            
#print result            
    
    
#check with the title tag    

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/titletoken.csv")

title = f.read()

#tokenize

ttoken = nltk.word_tokenize(title)

#lowercase
lower_title = [x.lower() for x in ttoken]

#compare with dict

for w in lower_title:

    result[w][1] = 1
    
#print result

#when title and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase2/ne.csv")

nestr = f.read()

tne = nltk.word_tokenize(nestr)

#lowercase all the ne words

lower_ne = [x.lower() for x in tne]

#compare with dict
for w in lower_ne:

    result[w][10] = 1
    
#print result


#title and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase2/noun_all.csv")

nounstr = f.read()

tnoun = nltk.word_tokenize(nounstr)

#lowercase all the ne words

lower_noun = [x.lower() for x in tnoun]

#compare with dict
for w in lower_noun:

    result[w][11] = 1
    
#print result


#title and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase2/caps.csv")

capstr = f.read()

tcap = nltk.word_tokenize(capstr)

#lowercase all the ne words

lower_cap = [x.lower() for x in tcap]

#compare with dict
for w in lower_cap:

    result[w][12] = 1
    
#print result


#h1

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/heading1.csv")

h1 = f.read()

th1 = nltk.word_tokenize(h1)

#lowercase all the h1 words

lower_h1 = [x.lower() for x in th1]

#compare with dict
for w in lower_h1:

    result[w][2] = 1
    
#print result


#when h1 and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase3/ne.csv")

neh1 = f.read()

tneh1 = nltk.word_tokenize(neh1)

#lowercase all the ne words

lowerh1_ne = [x.lower() for x in tneh1]

#compare with dict
for w in lowerh1_ne:

    result[w][10] = 1
    
#print result


#h1 and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase3/noun_all.csv")

h1noun = f.read()

tnounh1 = nltk.word_tokenize(h1noun)

#lowercase all the ne words

lowerh1_noun = [x.lower() for x in tnounh1]

#compare with dict
for w in lowerh1_noun:

    result[w][11] = 1
    
#print result


#title and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase3/caps.csv")

caph1 = f.read()

tcaph1 = nltk.word_tokenize(caph1)

#lowercase all the ne words

lowerh1_cap = [x.lower() for x in tcaph1]

#compare with dict

for w in lowerh1_cap:

    result[w][12] = 1
    
#print result

#h2

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/heading2.csv")

h2 = f.read()

th2 = nltk.word_tokenize(h2)

#lowercase all the h2 words

lower_h2 = [x.lower() for x in th2]

#compare with dict
for w in lower_h2:

    result[w][3] = 1
    
#print result


#when h2 and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase4/ne.csv")

neh2 = f.read()

tneh2 = nltk.word_tokenize(neh2)

#lowercase all the ne words

lowerh2_ne = [x.lower() for x in tneh2]

#compare with dict

for w in lowerh2_ne:

    result[w][10] = 1
    
#print result


#h2 and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase4/noun_all.csv")

h2noun = f.read()

tnounh2 = nltk.word_tokenize(h2noun)

#lowercase all the ne words

lowerh2_noun = [x.lower() for x in tnounh2]

#compare with dict

for w in lowerh2_noun:

    result[w][11] = 1
    
#print result


#h2 and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase4/caps.csv")

caph2 = f.read()

tcaph2 = nltk.word_tokenize(caph2)

#lowercase all the ne words

lowerh2_cap = [x.lower() for x in tcaph2]

#compare with dict

for w in lowerh2_cap:

    result[w][12] = 1
    
#print result


#h3

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/heading3.csv")

h3 = f.read()

th3 = nltk.word_tokenize(h3)

#lowercase all the h2 words

lower_h3 = [x.lower() for x in th3]

#compare with dict
for w in lower_h3:

    result[w][4] = 1
    
#print result


#when h3 and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase5/ne.csv")

neh3 = f.read()

tneh3 = nltk.word_tokenize(neh3)

#lowercase all the ne words

lowerh3_ne = [x.lower() for x in tneh3]

#compare with dict

for w in lowerh3_ne:

    result[w][10] = 1
    
#print result


#h3 and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase5/noun_all.csv")

h3noun = f.read()

tnounh3 = nltk.word_tokenize(h3noun)

#lowercase all the noun words

lowerh3_noun = [x.lower() for x in tnounh3]

#compare with dict

for w in lowerh3_noun:

    result[w][11] = 1
    
#print result


#h3 and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase5/caps.csv")

caph3 = f.read()

tcaph3 = nltk.word_tokenize(caph3)

#lowercase all the capitalized words

lowerh3_cap = [x.lower() for x in tcaph3]

#compare with dict

for w in lowerh3_cap:

    result[w][12] = 1
    
#print result

#h4

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/heading4.csv")

h4 = f.read()

th4 = nltk.word_tokenize(h4)

#lowercase all the h4 words

lower_h4 = [x.lower() for x in th4]

#compare with dict
for w in lower_h4:

    if w in result:
    
        result[w][5] = 1
     
    else:
        print result.get(w)                 
    
#print result


#when h4 and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase6/ne.csv")

neh4 = f.read()

tneh4 = nltk.word_tokenize(neh4)

#lowercase all the ne words

lowerh4_ne = [x.lower() for x in tneh4]

#compare with dict

for w in lowerh4_ne:

    if w in result:
    
        result[w][10] = 1
     
    else:
        print result.get(w)                 


#    result[w][10] = 1
    
#print result


#h4 and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase6/noun_all.csv")

h4noun = f.read()

tnounh4 = nltk.word_tokenize(h4noun)

#lowercase all the noun words

lowerh4_noun = [x.lower() for x in tnounh4]

#compare with dict

for w in lowerh4_noun:

    if w in result:
    
        result[w][11] = 1
     
    else:
        print result.get(w)                 




#    result[w][11] = 1
    
#print result


#h4 and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase6/caps.csv")

caph4 = f.read()

tcaph4 = nltk.word_tokenize(caph4)

#lowercase all the capitalized words

lowerh4_cap = [x.lower() for x in tcaph4]

#compare with dict

for w in lowerh4_cap:

    if w in result:
    
        result[w][12] = 1
     
    else:
        print result.get(w)                 


#    result[w][12] = 1
    
#print result


#h5

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/heading5.csv")

h5 = f.read()

th5 = nltk.word_tokenize(h5)

#lowercase all the h5 words

lower_h5 = [x.lower() for x in th5]

#compare with dict
for w in lower_h5:

    if w in result:
    
        result[w][6] = 1
     
    else:
        print result.get(w)                 


#    result[w][6] = 1
    
#print result


#when h5 and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase7/ne.csv")

neh5 = f.read()

tneh5 = nltk.word_tokenize(neh5)

#lowercase all the ne words

lowerh5_ne = [x.lower() for x in tneh5]

#compare with dict

for w in lowerh5_ne:

    if w in result:
    
        result[w][10] = 1
     
    else:
        print result.get(w)                 


#    result[w][10] = 1
    
#print result


#h5 and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase7/noun_all.csv")

h5noun = f.read()

tnounh5 = nltk.word_tokenize(h5noun)

#lowercase all the noun words

lowerh5_noun = [x.lower() for x in tnounh5]

#compare with dict

for w in lowerh5_noun:

    if w in result:
    
        result[w][11] = 1
     
    else:
        print result.get(w)                 



#    result[w][11] = 1
    
#print result


#h5 and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase7/caps.csv")

caph5 = f.read()

tcaph5 = nltk.word_tokenize(caph5)

#lowercase all the capitalized words

lowerh5_cap = [x.lower() for x in tcaph5]

#compare with dict

for w in lowerh5_cap:

    if w in result:
    
        result[w][12] = 1
     
    else:
        print result.get(w)                 



#    result[w][12] = 1
    
#print result



#h6

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/heading6.csv")

h6 = f.read()

th6 = nltk.word_tokenize(h6)

#lowercase all the h6 words

lower_h6 = [x.lower() for x in th6]

#compare with dict
for w in lower_h6:

    if w in result:
    
        result[w][7] = 1
     
    else:
        print result.get(w)                 

#    result[w][7] = 1
    
#print result


#when h6 and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase8/ne.csv")

neh6 = f.read()

tneh6 = nltk.word_tokenize(neh6)

#lowercase all the ne words

lowerh6_ne = [x.lower() for x in tneh6]

#compare with dict

for w in lowerh6_ne:

    if w in result:
    
        result[w][10] = 1
     
    else:
        print result.get(w)                 

#    result[w][10] = 1
    
#print result


#h6 and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase8/noun_all.csv")

h6noun = f.read()

tnounh6 = nltk.word_tokenize(h6noun)

#lowercase all the noun words

lowerh6_noun = [x.lower() for x in tnounh6]

#compare with dict

for w in lowerh6_noun:

    if w in result:
    
        result[w][11] = 1
     
    else:
        print result.get(w)                 


#    result[w][11] = 1
    
#print result


#h6 and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase8/caps.csv")

caph6 = f.read()

tcaph6 = nltk.word_tokenize(caph6)

#lowercase all the capitalized words

lowerh6_cap = [x.lower() for x in tcaph6]

#compare with dict

for w in lowerh6_cap:

    if w in result:
    
        result[w][12] = 1
     
    else:
        print result.get(w)                 


#    result[w][12] = 1
    
#print result

#for  urlnames

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/name.csv")

uname = f.read()

tuname = nltk.word_tokenize(uname)

#lowercase all the capitalized words

lower_uname = [x.lower() for x in tuname]

#compare with dict

for w in lower_uname:

    if w in result:
    
        result[w][8] = 1
     
    else:
        print result.get(w)                 

    
#print result

#when urlname and ne

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/ph2_urlname/ne.csv")

nename = f.read()

tnename = nltk.word_tokenize(nename)

#lowercase all the ne words

lowern_ne = [x.lower() for x in tnename]

#compare with dict

for w in lowern_ne:

    if w in result:
    
        result[w][10] = 1
     
    else:
        print result.get(w)                 

    
#print result


#urlname and noun

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/ph2_urlname/noun_all.csv")

nnoun = f.read()

tnnoun = nltk.word_tokenize(nnoun)

#lowercase all the noun words

lowern_noun = [x.lower() for x in tnnoun]

#compare with dict

for w in lowern_noun:

    if w in result:
    
        result[w][11] = 1
     
    else:
        print result.get(w)                 
    
#print result


#urlnames and caps

f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/ph2_urlname/urlcaps.csv")

ncap = f.read()

tncap = nltk.word_tokenize(ncap)

#lowercase all the capitalized words

lowern_cap = [x.lower() for x in tncap]

#compare with dict

for w in lowern_cap:

    if w in result:
    
        result[w][12] = 1
     
    else:
        print result.get(w)                 

    


print result


#storing the vector in a file

f = open("vector.csv", "w")

writer = csv.writer(f, dialect = 'excel')

for key, value in result.items():
    writer.writerow([key] + value)
    
f.close()    

#mapping from string to int for the list of values in the feature vector


for value in result.itervalues():

    valuenew = [float(x) for x in value]
    
#    value = valuenew[:]

       
    
#max ent classifier

from nltk.classify import MaxentClassifier

#feature set
'''
feat_set = {tfidf : '0.0' , title : 0.0 , h1 : 0.0 , h2 : 0.0 , h3 : 0.0 , h4 : 0.0 , h5 : 0.0 , h6 : 0.0 , uname : 0.0 , hypt : 0.0 , ne : 0.0 , noun : 0.0 , caps : 0.0}  
'''
#summing up the values for vectors
for key, val in result.items():

    sumval = 0;
   
    t = type(val)
    
#    print t 
    
    valnew = [float(x) for x in val]
    
    sumval = sum(valnew) 
    
#    print sumval
    
    result[key] = sumval;    #appending the sum of the features to the list of the values
    
    
#print result


#reverse sort the dictionary according to the sumval

from operator import itemgetter


#for key , val in sorted(result.items() , key = itemgetter(1), reverse = True ):

#    print(key, val)

resultnew = []

resultnew = sorted(result, key = result.__getitem__ , reverse = True)

#print resultnew

#storing this sorted list in a file

#removing words of length lesser than 3
final = [word for word in resultnew if len(word) >= 3]


#storing the sorted list in a csv file


f = open('keywords.csv', 'w')

f.write('\n'.join(final))

f.close
