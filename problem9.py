import sys
f= open(sys.argv[1],'r')
for b in f:
    a=b.find('\n')
    c=b[:a]
    n=c.split(" ")
    s=[]
    q=[]
    while len(n)>1:
        s.append(n.pop())
        q.append(n.pop())
    if len(n)==1:
        s.append(n.pop())
    print str(" ".join(s)) 
f.close()
