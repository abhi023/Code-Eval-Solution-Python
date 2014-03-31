import sys
f= open(sys.argv[1],'r')
for i in f:
     b=i.find('\n')
     a=i[:b]
     c=a.split(" ")
     c.reverse()
     print (" ".join(c))
    
f.close()