import sys
f= open(sys.argv[1],'r')
for b in f:
    b=b.strip()
    b=b.split(",")
    a,c=b[0],b[1]
    print a.find(c)
     
f.close()
