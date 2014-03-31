import sys
f= open(sys.argv[1],'r')
for b in f:
    a=b.find('\n')
    c=b[:a]
    counter=0
    if int(c)==int(c[::-1]):
           print counter, int(c)
    else:
        while int(c)!=int(c[::-1]):
             c=int(c)+int(c[::-1])
             c=str(c)
             counter=counter+1 
        print counter, int(c)                
f.close()
