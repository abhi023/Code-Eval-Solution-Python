import sys
f= open(sys.argv[1],'r')
for i in f:
      a=int(i)
      if a%2==0:
         print '1'
      else:
         print '0'
       
f.close()
