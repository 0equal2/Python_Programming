### 코드업 #2605
### 캔디팡


from collections import deque


def dfs(x,y,board,check):
    queue=deque()
    queue.append([x,y])
    check[x][y]=1

    color=board[x][y]

    count=1
    
    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx and nx<7 and 0<=ny and ny<7:
                #같은 색상이면서 아직 탐색이 되지 않으면 탐색
                if board[nx][ny]==color and check[nx][ny]==0: 
                    check[nx][ny]=1
                    queue.append([nx,ny])
                    count+=1


    if count>=3:
        return 1
    else:
        return 0


        


#1. board 입력
board=[]

for i in range(7):
    board.append(list(map(int,input().split())))


#2. 탐색 체크
check=[[0 for x in range(7)] for y in range(7)]


#3. 탐색 방향
global dx,dy
dx=[0,0,1,-1]
dy=[1,-1,0,0]


#4. 탐색 시작
count=0

for i in range(7):
    for j in range(7):
        if check[i][j]==0:
            if dfs(i,j,board,check):
                count+=1

print(count)



        
