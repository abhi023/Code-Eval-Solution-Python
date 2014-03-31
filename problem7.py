import sys
f= open(sys.argv[1],'r')
for b in f:
    a=b.find('\n')
    c=b[:a]
    print bin(int(c))[2:]
                          
f.close()
