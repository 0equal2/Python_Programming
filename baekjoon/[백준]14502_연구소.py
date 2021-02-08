### 백준 #14502
### 연구소


from sys import stdin
from collections import deque
from itertools import combinations

def bfs(x,y,b,c):
    count=0
    
    queue=deque()
    queue.append([x,y])
    c[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(len(dx)):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx and nx<n and 0<=ny and ny<m:
                if b[nx][ny]==0 and c[nx][ny]==0:
                    c[nx][ny]=1
                    count+=1
                    queue.append([nx,ny])
    
    return count


#1. n,m
n,m = map(int,stdin.readline().split())

#2. 지도 정보
board=[] #지도 정보 맵
for i in range(n):
    data=list(map(int,stdin.readline().split()))
    board.append(data)
    

#3. 벽을 세울 수 있는 공간 (0인 자리를 구하면서 안전 구역 수 카운트)
wall=[]
safe=-3  #안전 구역 개수=0의 개수 (나중에 벽을 3개 세울것이기 때문에 -3)
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            wall.append([i,j])
            safe+=1

#4. 벽을 세울 수 있는 경우의 수
wall=list(combinations(wall,3))
#print(wall[0])


#5. bfs 탐색

result=[]

#5-1. 방향 벡터
dx=[0,0,1,-1]
dy=[1,-1,0,0]


for x,y,z in wall:
    
    #5-2. 새로운 벽 설치
    board[x[0]][x[1]]=1
    board[y[0]][y[1]]=1
    board[z[0]][z[1]]=1

    
    #5-3. check
    check=[[0 for i in range(m)] for j in range(n)]

    count=safe

    #print(new_board)

    #5-4. 바이러스 탐색 시작
    for i in range(n):
        for j in range(m):
            
            if board[i][j]==2 and check[i][j]==0:
                count-=bfs(i,j,board,check)
                

    #5-5. 안전지대 개수 세기
    result.append(count)

    #5-6. 벽 세웠던 곳을 다시 0으로 되돌려놓음 
    board[x[0]][x[1]]=0
    board[y[0]][y[1]]=0
    board[z[0]][z[1]]=0
    


print(max(result))
                
            
    
    
