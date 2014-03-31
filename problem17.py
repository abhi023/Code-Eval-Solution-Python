import sys
f= open(sys.argv[1],'r')
for i in f:
       c=list(i)
       a=c.pop()
       sum=[]
       for el in c:
          if el.isalpha():
              if el.isupper():
                  p=el.lower()
                  sum.append(p)
              else:
                  p=el.upper()
                  sum.append(p)
          else:
              sum.append(el) 
       sum.append(a)
       print "".join(sum)   
       
f.close()