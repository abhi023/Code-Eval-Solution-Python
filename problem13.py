import sys
f= open(sys.argv[1],'r')
for i in f:
      n=i.find('\n')
      b=i[:n]
      a=b.split("|")
      b=(a[0]).split(" ")
      c=(a[1]).split(" ")
      s=[]
      q=[] 
      for i in b:
            if i.isdigit():
		       s.append(i)
      for i in c:
        	if i.isdigit():
		       q.append(i)
      s=map(int,s)
      q=map(int,q)
      lis=[]
      for i in range(0,len(s)):
             mul=s[i]*q[i]
             lis.append(mul)
      lis=map(str,lis)
      print " ".join(lis)     
f.close()