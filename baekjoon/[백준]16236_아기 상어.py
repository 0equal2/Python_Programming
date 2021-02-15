### 백준 #16236
### 아기 상어

from sys import stdin
from collections import deque

def bfs(x,y,m,space,size):
    fishlist=[]
    
    q=deque()
    q.append([m,x,y])
    check=[[0 for i in range(n)] for j in range(n)]
    check[x][y]=1
    

    while q:
        m,x,y=q.popleft()
        
        
        for i in range(len(dx)):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n:
                if check[nx][ny]==0:
                    check[nx][ny]=1

                    if space[nx][ny]==0 or space[nx][ny]==size:
                        q.append([m+1,nx,ny])
                    
                    if space[nx][ny]!=0 and space[nx][ny]<size:
                        fishlist.append([m+1,nx,ny])

                    
    
    return fishlist
    

#1. n
n=int(stdin.readline())

#2. space, 아기상어 현재 위치
space=[]
x,y=0,0

for i in range(n):
    line=list(map(int, stdin.readline().split()))
    space.append(line)

    #아기상어 위치
    if 9 in line:
        x=i
        y=line.index(9)

space[x][y]=0
    
#3. 
dx=[0,0,1,-1]
dy=[1,-1,0,0]


#4.
size=2
fish=0
move=0

queue=deque()
queue.append([x,y])

while queue:
    x,y=queue.popleft()

    #if size==fish:
    #    size+=1
    #    fish=0

    fishlist=bfs(x,y,0,space,size)

    #더 이상 먹을 수 있는 물고기가 공간에 없다
    if not fishlist:
        break

    #가장 가까우면서 위이면서 왼쪽인 먹이
    fishlist=sorted(fishlist)

    #
    fm,fx,fy=fishlist[0]
    move+=fm
    space[fx][fy]=0
    fish+=1

    if size==fish:
        size+=1
        fish=0
    
    queue.append([fx,fy])

print(move)
