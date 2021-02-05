### 코드업 #2610
### 그림판 채우기


from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    draw[x][y]='*'
    check[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(len(dx)):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx and nx<n and 0<=ny and ny<n:
                if draw[nx][ny]=='_' and check[nx][ny]==0:
                    check[nx][ny]==1
                    draw[nx][ny]='*'
                    queue.append([nx,ny])


#1.
n=10 # 10x10 사이즈


#2. 그림판 정보
draw=[]

for i in range(n):
    draw.append(list(map(str,input())))


#3. 시작 점
y,x=map(int,input().split())



#4. 방향 벡터
dx=[0,0,1,-1]
dy=[1,-1,0,0]



#5.
check=[[0 for x in range(n)] for y in range(n)]


#6. 시작 점이 색칠되어있지 않은 곳일 경우
if draw[x][y]=='_':
    bfs(x,y)


#7. 색칠 결과 출력
for i in range(n):
    print(''.join(draw[i]))
