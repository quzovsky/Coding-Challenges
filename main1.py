import math
tc=int(input())
l=[]
ans=[]
for i in range(0,tc):
    l.append(int(input()))
    count=0
    c=l[i]
    for a in range(1,c):
        b=(c**2)-(a**2)
        if b>0:
            m=math.sqrt(b)
            if float(m)==int(m):
                count+=1
    ans.append(int(count/2))
for i in range(0,tc):
    print(ans[i])
