import sys
f= open(sys.argv[1],'r')
for i in f:
       c=list(i)
       c.pop()
       a=len(c)
       sum=0
       for el in c:
          sum+=int(el)**a
       if sum==int(i):
           print 'True'
       else:
           print 'False'
          
       
f.close()
