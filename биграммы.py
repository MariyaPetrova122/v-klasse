f=open('Genproc.csv','r', encoding='UTF-8')
genproc = []
for line in f:
    a = line.split()
    i=0
    while i<5:
        a.remove(a[0])
        i+=1
    genproc.extend(a)
print(genproc)
f.close()
bigrams = []
i=0
while i<len(words)-1:
    w1 = words[i]
    w2=words[i+1]
    bigrams.append(w1+' '+w2
