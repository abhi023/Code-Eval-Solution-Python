import sys
f= open(sys.argv[1],'r')
for b in f:
    b=b.strip()
    b=list(b)
    c=[]
    for i in b:
        if b.count(i)==1:
           c.append(i)
    print c[0]
     
f.close()
