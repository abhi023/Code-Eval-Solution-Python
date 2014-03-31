import sys
f= open(sys.argv[1],'r')
for b in f:
     print str(list(bin(int(b))).count('1'))     
f.close()
