n,k=map(int,input().split(' '))
stat={}
kstat=['FREE']*k
for i in range(n):
    id=input()
    stat[id]=1
def take_off(id,stat,kstat):
    statlist=list(stat.keys())
    if id in statlist:
        if stat[id]==1:
            if kstat.count('FREE')==0:
                return('NO FREE BOUND')
            else:
                stat[id]=2
                kstat[kstat.index('FREE')]=id
        elif stat[id]==2:
            return('YOU ARE TAKING OFF')
        elif stat[id]==3:
            return('YOU ARE LANDING NOW')
    else:
        return('YOU ARE NOT HERE')
def landing(id,stat,kstat):
    statlist=list(stat.keys())
    if id in statlist:
        if stat[id]==1:
            return('YOU ARE HERE')
        elif stat[id]==2:
            return('YOU ARE TAKING OFF')
        elif stat[id]==3:
            return('YOU ARE LANDING NOW')
    else:
        if kstat.count('FREE')==0:
            return('NO FREE BOUND')
        else:
            stat[id]=3
            kstat[max(loc for loc, val in enumerate(kstat) if val == 'FREE')]=id
report=[]
q=int(input())
for i in range(q):
    order,id=map(str,input().split(' '))
    if len(id)==10:
        if order=='TAKE-OFF':
            report.append(take_off(id,stat,kstat))
        elif order=='LANDING':
            report.append(landing(id,stat,kstat))
        elif order=='PLANE-STATUS':
            if id in stat:
                report.append(stat[id])
            else:
                report.append(4)
    else:
        if order=='BAND-STATUS':
            report.append(kstat[int(id)-1])
for i in range(len(report)):
    if report[i]!=None:
        print(report[i])
#https://quera.org/contest/assignments/44345/problems/148508
