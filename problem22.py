import sys
f= open(sys.argv[1],'r')
sum=0
contents=f.readlines()
for i in contents:
    sum=sum+int(i)
print sum
f.close()