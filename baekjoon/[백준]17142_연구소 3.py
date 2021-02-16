### 백준 #17142
### 연구소 3


from itertools import combinations
from collections import deque
import sys
sys.setrecursionlimit(10**6)


def bfs(virus, check, lab, count, move):

    if count==nonvirus:
        return move

    if not virus:
        return -1
    
    
    queue=deque()
    newvirus=[]

    for i in virus:
        queue.append(i)
        check[i[0]][i[1]]=1

    while queue:
        x,y=queue.popleft()

        for i in range(len(dx)):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if lab[nx][ny]!=1 and check[nx][ny]==0:
                    newvirus.append([nx,ny])
                    check[nx][ny]=1

                    if lab[nx][ny]==0:
                        count+=1

    return bfs(newvirus,check,lab,count,move+1)
        



#1. 연구실 크기, 활성 바이러스 개수 : n, m
n,m=map(int,sys.stdin.readline().split())

#2. 연구실 정보
lab=[]

for i in range(n):
    lab.append(list(map(int,sys.stdin.readline().split())))

#3. 바이러스 위치, 바이러스가 아닌 위치(벽제외)
global nonvirus
virus=[]
nonvirus=0


for i in range(n):
    for j in range(n):
        if lab[i][j]==2:
            virus.append([i,j])
        elif lab[i][j]==0:
            nonvirus+=1


#print(virus)

#4. 바이러스 활성 경우의 수
activation=list(combinations(virus,m))


#5.
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#6.
result=[]

for case in activation:
    check=[[0 for x in range(n)] for y in range(n)]

    move=bfs(case,check,lab,0,0)

    if move!=-1:
        result.append(move)

if result:
    print(min(result))
else:
    print(-1)
