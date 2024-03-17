N,M,P,C,D = map(int,input().split())
rR,rC = map(int,input().split())
rR-=1
rC-=1
S = [[] for _ in range(P)]
for _ in range(P):
    idx,r,c = map(int,input().split())
    S[idx-1] = [r-1,c-1]
def dis(r1,c1,r2,c2):
    return (r1-r2)**2 + (c1-c2)**2
def pickSanta():
    global rR,rC
    return min([[dis(rR,rC,S[i][0],S[i][1]),-S[i][0],-S[i][1],i] for i in range(P) if state[i]!=-1])
def moveRodolph():
    global rR,rC,turn
    tar,_,_,Tidx = pickSanta()
    tr,tc = S[Tidx]
    Nr, Nc = 0, 0
    Dr,Dc = 0,0
    Dis = 1000000000
    move = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(8):
        dr, dc = move[i]
        nr,nc = rR+dr,rC+dc
        if not (0<=nr<N and 0<=nc<N): continue
        newDis = dis(nr,nc,tr,tc)
        if newDis<Dis:
            Nr,Nc = nr, nc
            Dis = newDis
            Dr,Dc = dr,dc
    rR, rC = Nr,Nc
    if [rR,rC] == [tr,tc] :
        state[Tidx] = turn + 1
        collision(Tidx, C,[Dr,Dc])
def interAction(Sidx,Dir):
    r, c = S[Sidx]
    dr, dc = Dir
    nr,nc = r+dr,c+dc
    if not (0<=nr<N and 0<=nc<N):
        state[Sidx]=-1
        S[Sidx] = [-1,-1]
    else:
        if [nr,nc] in S:
            bak = S.index([nr,nc])
            S[Sidx] = [nr,nc]
            interAction(bak,Dir)
        else:S[Sidx] = [nr,nc]
def collision(Sidx,getS,Dir):
    global turn
    score[Sidx] += getS
    nr,nc = S[Sidx]
    nr += getS*Dir[0]
    nc += getS*Dir[1]
    if not (0<=nr<N and 0<=nc<N):
        state[Sidx] = -1
        S[Sidx] = [-1,-1]
    elif [nr,nc] in S:
        bak = S.index([nr,nc])
        S[Sidx] = [nr,nc]
        interAction(bak,Dir)
    else: S[Sidx] = [nr,nc]
def moveSanta(Sidx):
    global rR,rC,turn
    if state[Sidx]==-1:return
    if state[Sidx]>=turn:return
    r,c = S[Sidx]
    Nr, Nc = 0, 0
    Dr,Dc = 0,0
    Dis = dis(r,c,rR,rC)
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    for i in range(4):
        dr, dc = move[i]
        nr,nc = r+dr,c+dc
        if not (0<=nr<N and 0<=nc<N): continue
        if [nr,nc] in S:continue
        newDis = dis(nr,nc,rR,rC)
        if newDis<Dis:
            Nr,Nc = nr, nc
            Dis = newDis
            Dr,Dc = dr,dc
    if Dis == dis(r,c,rR,rC):return
    S[Sidx] = [Nr,Nc]
    if [rR,rC] == [Nr,Nc] :
        state[Sidx] = turn+1
        collision(Sidx, D,[-Dr,-Dc])
state = [0]*P # -1 탈락, 0 정상, x x에 기절
score = [0]*P
turn = 1
while turn<=M:
    moveRodolph()
    if all([x==-1 for x in state]):
        break
    for i in range(P):
        moveSanta(i)
        if all([x==-1 for x in state]):
            P = -1
            M=0
            break
    for i in range(P):
        if state[i]!=-1:
            score[i]+=1
    turn+=1
print(*score)