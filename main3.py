tc=int(input())
ans=[]
def minblock(n,m,a,b):
    counter1=0
    counter2=0
    c=n
    while c>0:
        c-=a
        if c>=0:
            counter1+=1
        c-=(a-1)
    c1=m
    while c1>0:
        c1-=b
        if c1>=0:
            counter2+=1
        c1-=(b-1)
    return(counter1*counter2)
for t in range(0,tc):
    l=input().split(' ')
    n=int(l[0])
    m=int(l[1])
    a=int(l[2])
    b=int(l[3])
    ans.append(minblock(n,m,a,b))
for i in range(0,tc):
    print(ans[i])
