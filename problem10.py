import sys
f= open(sys.argv[1],'r')
for i in f:
       b=i.find('\n')
       a=i[:b]
       c=a.split(" ")
       n=c.pop()
       if int(n)<len(c) or int(n)==len(c):
           print str(c[-(int(n))])   
f.close()
