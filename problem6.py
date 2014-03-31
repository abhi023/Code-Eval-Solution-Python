import sys
f= open(sys.argv[1],'r')
for b in f:
    a=b.find('\n')
    c=b[:a]
    n=c.split(", ")
    text=n[0]
    pattern=n[1]
    for el in list(n[1]):
        text=text.replace(el,"")
    print text 
                          
f.close()
