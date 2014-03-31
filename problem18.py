import sys
f= open(sys.argv[1],'r')
for i in f:
     n=i.split(" ")
     a,b,c=int(n[0]),int(n[1]),int(n[2])
     for e in range(1,c+1):
        if e%a==0 and e%b==0:
           print 'FB',
        elif e%a==0:
                print 'F',
        elif e%b==0:
               print 'B',
        else:
           print e,
     print "\n" 

f.close()
