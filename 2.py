n=int(input())
s=input()
k=int(input())
def result(s,k,num):
    l=[]
    kl=list(k)
    for i in s:
        if i=='A':
            l.append(0)
        if i=='B':
            l.append(1)
        if i=='C':
            l.append(2)
        if i=='D':
            l.append(3)
    if kl.count('#')==1:
        if kl.index('#')==l[num]:
            return('t')
        else:
            return('f')
    elif kl.count('O')==4:
        return('Empty')
    else:
        return('f')
results=[]
for i in range(k):
    resultk=[]
    for j in range(n):
        k1=input()
        resultk.append(result(s,k1,j))
    results.append((3*resultk.count('t'))-(resultk.count('f')))
for i in range(k):
    print(results[i])
#https://quera.org/contest/assignments/44345/problems/148511
