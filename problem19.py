def prime(n):
    i=1
    p=[]
    if n>1:
        p.append(2)
    while len(p)<n:
        b=2
        while b<i:
             if i%b==0:
                 break;   
             if i-1==b:
                 p.append(i)
             b +=1
        i=i+1     
    return p

        
def prime_sum(b):
    sum=0
    for e in b:
        sum +=e
    return sum

a=prime(1000)
print (prime_sum(a))
