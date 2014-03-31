import sys
f= open(sys.argv[1],'r')
for b in f:
    a=b.find('\n')
    c=b[:a]
    d=c.split(" ")
    e=len(d)
    n=d[e-2]
    print n              
f.close()
