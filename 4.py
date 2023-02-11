n,q=map(int,input().split(' '))
s=list(input().split(' '))
for i in range(len(s)):
    s[i]=int(s[i])
ans=[]
for i in range(q):
    order,val1,val2=map(str,input().split(' '))
    val1=int(val1)
    val2=int(val2)
    if order=='+':
        s[val1-1]=val2
    elif order=='?':
        sum=0
        endp=max(s[val1-1:val2])
        startp=min(s[val1-1:val2])
        l=list(range(startp,endp+1))
        for j in l:
            if s[val1-1:val2].__contains__(j):
                sum+=1
            else:
                ans.append('NO')
                break
        if sum==len(l):
            if l.__contains__(val2-val1+1) and l.__contains__(1):
                ans.append('YES')  
            else:
                ans.append('NO')
for i in range(len(ans)):
    print(ans[i])
#https://quera.org/contest/assignments/44345/problems/148507
