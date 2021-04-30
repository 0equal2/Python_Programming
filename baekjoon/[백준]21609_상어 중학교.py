###백준 #21609
###상어 중학교

from collections import deque

#격자를 90도 반시계방향으로 회전
def rotate(board):
    newboard=[[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            newboard[n-j-1][i]=board[i][j]

    return newboard

#격자에 중력이 작용
def gravity(board):
    #맨 아래 줄부터 중력 작용
    for i in range(n-1,-1,-1):
        for j in range(n):
            if board[i][j]>=0:
                r=i
                while True:
                    if 0<=r+1<n:
                        if board[r+1][j]==-2:
                            board[r+1][j]=board[r][j]
                            board[r][j]=-2
                            r+=1
                        else:
                            break
                    else:
                        break
                 
                
                    


#선택된 블럭을 캐는 함수
def blockout(block_info,board):
    for x,y in block_info:
        board[x][y]=-2



#크기가 가장 큰 블록 그룹을 찾는 함수
def bfs(x,y,board,check):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    queue=deque()
    queue.append([x,y])
    check[x][y]=1
    color=board[x][y]

    block_size=1 #블럭 사이즈
    block_info=[[x,y]] #블럭 정보

    rainbow=0 #무지개 블럭 포함 수
    rainbow_info=[]

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if (board[nx][ny]==0 or board[nx][ny]==color) and check[nx][ny]==0:
                    block_size+=1
                    

                    if board[nx][ny]==0:
                        rainbow+=1
                        rainbow_info.append([nx,ny])
                    else:
                        block_info.append([nx,ny])
                        
                    check[nx][ny]=1
                    queue.append([nx,ny])

    #무지개 블럭은 다시 방문 check를 풀어줘야한다.
    for x,y in rainbow_info:
        check[x][y]=0

    return [block_size,rainbow,sorted(block_info)+rainbow_info]

    
    
#캘 수 있는 모든 블럭 찾는 함수
def block_search(board):
    check=[[0 for i in range(n)] for j in range(n)]
    rainbowcheck=[[0 for i in range(n)] for j in range(n)]

    block=[]

    for i in range(n):
        for j in range(n):
            if board[i][j]>0 and check[i][j]==0:
                block_info=bfs(i,j,board,check)
                #블럭의 크기가 2보다 커야함.
                if block_info[0]>=2:
                    block.append(block_info)

    
    return sorted(block,key=lambda t : (-t[0],-t[1],-t[2][0][0],-t[2][0][1]))

    



#1. 격자의 크기 : n / 색상의 개수 : m
n,m=map(int,input().split())

#2. 격자 정보 생성
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

#3.
score=0

while True:
    #3-1. 크기가 가장 큰 블록 그룹을 찾는다. 캘 수 있는 블록이 없으면 종료
    block=block_search(board)
    if not block:
        break

    #3-2. 3-1에서 찾은 블록 그룹의 모든 블록을 제거한다. 그리고 size**2만큼 점수 획득
    blockout(block[0][2],board)
    score+=block[0][0]**2
    
    #3-3. 격자에 중력이 작용
    gravity(board)

    #3-4. 격자가 90도 반시계 방향으로 회전
    board=rotate(board)
    
    #3-5. 다시 격자에 중력이 작용
    gravity(board)
    
print(score)
