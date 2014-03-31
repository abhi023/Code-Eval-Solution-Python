import sys
f= open(sys.argv[1],'r')
for i in f:
       c=i.find('\n')
       b=i[:c]
       a=list(b)
       sum=0
       for el in a:
           a=int(el)
           sum+=a   
       
       print sum  
f.close()