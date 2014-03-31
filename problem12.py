import sys
f= open(sys.argv[1],'r')
for b in f:
     a=b.find('\n')
     d=b[:a]
     coin=0
     c=int(d)
     while c>5 or c==5:
           coin+=1
           c-=5
     while c>3 or c==3:
           coin+=1
           c-=3
     while c!=0:
           coin+=1
           c-=1
     print str(coin)       
f.close()
