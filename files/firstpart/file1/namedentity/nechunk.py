import nltk


sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked",
"VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]

pattern = "NP: {<DT>?<JJ>*<NN>}"  #a typical noun phrase


NPChunker = nltk.RegexpParser(pattern) # create a chunk parser


result = NPChunker . parse(sentence) # parse the example sentence

print result

result.draw()
