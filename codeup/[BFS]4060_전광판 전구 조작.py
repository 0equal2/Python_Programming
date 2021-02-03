### 코드업 #4069
### 전광판 전구 조작


from collections import deque


def on_dfs(x,y,check,board):
    queue=deque()
    queue.append([x,y])

    check[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx and nx<m and 0<=ny and ny<n:
                if board[nx][ny]==0 and check[nx][ny]==0:
                    check[nx][ny]=1
                    queue.append([nx,ny])



def off_dfs(x,y,check,board):
    queue=deque()
    queue.append([x,y])

    check[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx and nx<m and 0<=ny and ny<n:
                if board[nx][ny]==1 and check[nx][ny]==0:
                    check[nx][ny]=1
                    queue.append([nx,ny])


            
#1. m,n 입력
global m,n
m,n=map(int,input().split())

#2. board 입력
board=[]

for i in range(m):
    board.append(list(map(int,input().split())))


global dx, dy
dx=[0,0,1,-1]
dy=[1,-1,0,0]


#3. 모든 전구 on
on_check=[[0 for x in range(n)] for y in range(m)]
on_count=0

for i in range(m):
    for j in range(n):
        if board[i][j]==0 and on_check[i][j]==0:
            on_dfs(i,j,on_check,board)
            on_count+=1


#4. 모든 전구 off
off_check=[[0 for x in range(n)] for y in range(m)]
off_count=0


for i in range(m):
    for j in range(n):
        if board[i][j]==1 and off_check[i][j]==0:
            off_dfs(i,j,off_check,board)
            off_count+=1
            
print(on_count,off_count)
