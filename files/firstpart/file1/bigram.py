import nltk
from nltk.tokenize import *
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def bag_of_words(words):
    return dict([(word, True) for word in words])


def bigram_words(words, score_fn = BigramAssocMeasures.chi_sq, n=200):

    bigram_finder = BigramCollocationFinder.from_words(words)
    
    bigrams = bigram_finder.nbest(score_fn, n)
    
    return bag_of_words(words + bigrams)
    
    
f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/firstpart/file1/phase1/raw_new.csv")   

string = f.read()

f.close()

words = nltk.word_tokenize(string)


bigrams = {}

bigrams = bigram_words(words)


print bigrams 


    
