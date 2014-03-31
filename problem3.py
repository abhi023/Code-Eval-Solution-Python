import sys
f= open(sys.argv[1],'r')
for b in f:
    b=b.strip()
    b= b.split(",")
    a=[]
    c=[]
    for i in b:
        if i.isdigit():
           a.append(i)
    for i in b:
        if i.isalpha():
           c.append(i)
    if len(a)>0 and len(c)>0:
        print ",".join(c)+'|'+",".join(a)
    else:
        print ",".join(a+c)  
f.close()
