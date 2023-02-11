t=int(input())
ans=[]
def result(sumest,sumpers):
    if sumpers==sumest:
        if b>c:
            return('esteghlal')
        elif c>b:
            return('perspolis')
        elif b==c:
            return('penalty')
    else:
        if sumest>sumpers:
            return('esteghlal')
        else:
            return('perspolis')
for i in range(t):
    a,b,c,d=map(int,input().split(' '))
    sumpers=a+c
    sumest=b+d
    ans.append(result(sumest,sumpers))
for i in range(len(ans)):
    print(ans[i])
    #https://quera.org/contest/assignments/44345/problems
