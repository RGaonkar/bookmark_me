f = open("/media/34227B6E227B3448/projectBooKmarks/mid_sem/phase1/raw.txt")

raw = f.read()

t = type(raw)

print (t)


raw = raw.decode("utf-8")

raw = raw.replace(u"\u2018", "").replace(u"\u2019", "").replace(u"\u201c","").replace(u"\u201d", "")	

#print (raw)


f = open("raw_new.txt", "w")
f.write(raw)
f.close()

