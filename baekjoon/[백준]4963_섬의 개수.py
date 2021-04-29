###백준 #4963
###섬의 개수

from collections import deque

def bfs(x,y,check,board):
    dx=[0,0,1,-1,1,1,-1,-1]
    dy=[1,-1,0,0,1,-1,1,-1]

    queue=deque([[x,y]])
    check[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(len(dx)):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if check[nx][ny]==0 and board[nx][ny]==1:
                    check[nx][ny]=1
                    queue.append([nx,ny])


while True:
    #1. 가로, 세로 : m,n
    m,n=map(int,input().split())

    #2. 0 0 입력이면 testcase종료
    if n==0 and m==0:
        break

    #3. 지도 정보
    board=[]
    for i in range(n):
        board.append(list(map(int,input().split())))

    #4. 방문 체크
    check=[[0 for i in range(m)] for j in range(n)]

    #5.
    count=0
    
    for i in range(n):
        for j in range(m):
            if board[i][j]==1 and check[i][j]==0:
                bfs(i,j,check,board)
                count+=1
    print(count)

    

    
