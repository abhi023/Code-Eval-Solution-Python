import sys
f= open(sys.argv[1],'r')
contents=f.readlines()
for i in contents:
    print i.lower()

f.close()
