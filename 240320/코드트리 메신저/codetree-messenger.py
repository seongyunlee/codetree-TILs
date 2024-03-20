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
def toggleAlarm(idx):
    alarm[idx] = not alarm[idx]
def changeAuth(idx,N):
    authority[idx] = N
def changeParent(a,b):
    pb,pa = parent[b],parent[a]
    parent[b], parent[a] = pa,pb
    child[pb].remove(b)
    child[pb].append(a)
    child[pa].remove(a)
    child[pa].append(b)
def query(idx):
    Q = child[idx]
    cnt = 0
    depth = 1
    while Q:
        nq = []
        for q in Q:
            if not alarm[q]:continue
            if depth<=authority[q]:
                cnt+=1
            for qq in child[q]:
                nq.append(qq)
        Q = nq
        depth+=1
    return cnt
for _ in range(Q-1):
    M,*args = map(int,input().split())
    if M==200:
        toggleAlarm(*args)
    elif M==300:
        changeAuth(*args)
    elif M==400:
        changeParent(*args)
    else:
        print(query(*args))