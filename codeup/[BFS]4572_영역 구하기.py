### 코드업 #4572
### 영역 구하기


from collections import deque

def bfs(x,y,board):
    queue=deque()
    queue.append([x,y])
    board[x][y]=1

    size=1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx and nx<n and 0<=ny and ny<m:
                if board[nx][ny]==0:
                    board[nx][ny]=1
                    queue.append([nx,ny])

                    size+=1

    return size

        
    
    


#1. 열, 행, 직사각형 수
global m,n
m, n, box = map(int,input().split())


#2. board 생성
board=[[0 for x in range(m)] for y in range(n)]

#3. 직사각형이 칠해진 부분 1로 칠하기
for i in range(box):
    lx,ly,rx,ry=map(int, input().split())

    for j in range(lx,rx):
        for k in range(ly,ry):
            board[j][k]=1

#print(board)

#4. 탐색 방향 벡터
global dx,dy
dx=[0,0,1,-1]
dy=[1,-1,0,0]


#4. 분리된 사각형 개수와 크기 구하기
size=[]
count=0

for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            size.append(bfs(i,j,board))
            count+=1



print(count)
size=list(map(str,sorted(size)))
print(' '.join(size))
