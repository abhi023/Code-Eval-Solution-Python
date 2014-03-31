import sys
f= open(sys.argv[1],'r')
for b in f:
    a=b.find('\n')
    c=b[:a]
    d=c.split(",")
    m,n=d[0],d[1]
    m=m.split(" ")
    n=n.split(" ")
    l=len(n)
    if m[-l:]==n:
       print "1" 
    else:
       print "0"        
f.close()
