import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
K = list(map(int,input().split()))
parent = [None] + K[1:N+1]
child = [[] for _ in range(N+1)]
for i in range(1,len(parent)):
    child[parent[i]].append(i)
authority = [None] + K[N+1:]
alarm = [True]*(N+1)
S = [{} for _ in range(N+1)]
SS = [0]*(N+1)
def sumDict(a,b):
    s = dict(a)
    for k,v in b.items():
        if k in s:
            s[k]+=v
        else:s[k]=v
    return s
def update(idx):
    S[idx] = {}
    CC = [S[i] for i in child[idx] if alarm[i]]
    if len(CC)==2:   
        sumChild = sumDict(*CC) 
        for k,v in sumChild.items():
            if k-1<0:continue
            S[idx][k-1] = v
    elif len(CC)==1:
        for k,v in CC[0].items():
            if k-1<0:continue
            S[idx][k-1] = v
    if idx==0:return
    if S[idx].get(min(20,authority[idx]))==None:
        S[idx][min(20,authority[idx])]=1
    else:
        S[idx][min(20,authority[idx])]+=1
    SS[idx] = query(idx)
    if idx!=0:update(parent[idx])
def makeInfo(idx):
    CC = [makeInfo(i) for i in child[idx] if alarm[i]]
    if len(CC)==2:   
        sumChild = sumDict(*CC) 
        for k,v in sumChild.items():
            if k-1<0:continue
            S[idx][k-1] = v
    elif len(CC)==1:
        for k,v in CC[0].items():
            if k-1<0:continue
            S[idx][k-1] = v
    if idx==0:
        SS[idx] = query(idx)
        return
    if S[idx].get(min(20,authority[idx]))==None:
        S[idx][min(20,authority[idx])]=1
    else:
        S[idx][min(20,authority[idx])]+=1
    SS[idx] = query(idx)
    return S[idx]
def toggleAlarm(idx):
    alarm[idx] = not alarm[idx]
    update(idx)
def changeAuth(idx,N):
    authority[idx] = N
    update(idx)
def changeParent(a,b):
    pb,pa = parent[b],parent[a]
    parent[b], parent[a] = pa,pb
    child[pb].remove(b)
    child[pb].append(a)
    child[pa].remove(a)
    child[pa].append(b)
    update(pa)
    update(pb)
def query(idx):
    return sum(S[idx].values())-(1 if idx!=0 else 0)
makeInfo(0)
for _ in range(Q-1):
    M,*args = map(int,input().split())
    if M==200:
        toggleAlarm(*args)
    elif M==300:
        changeAuth(*args)
    elif M==400:
        changeParent(*args)
    else:
        print(SS[args[0]])