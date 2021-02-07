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
                    #print("**",nx,ny)
                    count+=1
                    queue.append([nx,ny])
    #print("----",count)
    return count


#1. n,m
n,m = map(int,stdin.readline().split())

#2. 지도 정보
board=[]
safe=-3
for i in range(n):
    data=list(map(int,stdin.readline().split()))
    board.append(data)
    safe+=data.count(0)

#3. 벽을 세울 수 있는 공간
wall=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            wall.append([i,j])

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
    new_board=board
    new_board[x[0]][x[1]]=1
    new_board[y[0]][y[1]]=1
    new_board[z[0]][z[1]]=1

    
    #5-3. check
    check=[[0 for i in range(m)] for j in range(n)]

    count=safe

    #print(new_board)

    #5-4. 바이러스 탐색 시작
    for i in range(n):
        for j in range(m):
            
            if new_board[i][j]==2 and check[i][j]==0:
                count-=bfs(i,j,new_board,check)
                #print(i,j,count)

    #5-5. 안전지대 개수 세기
    result.append(count)


    new_board[x[0]][x[1]]=0
    new_board[y[0]][y[1]]=0
    new_board[z[0]][z[1]]=0
    


print(max(result))
                
            
    
    
