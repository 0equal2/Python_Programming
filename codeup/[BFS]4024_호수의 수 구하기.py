### 코드업 #4024
### 호수의 수 구하기


from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    check[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx and nx<h and 0<=ny and ny<w:
                if lack[nx][ny]=='L' and check[nx][ny]==0:
                    check[nx][ny]=1
                    queue.append([nx,ny])




#1. 지도의 너비, 높이 w,h
global w,h
w,h=map(int,input().split())


#2. 호수 지도 생성
global lack
lack=[]

for i in range(h):
    lack.append(list(map(str,input().split())))


#3. 방향 벡터 (대각선까지 추가)
global dx, dy
dx=[0,0,1,-1,1,-1,1,-1]
dy=[1,-1,0,0,1,-1,-1,1]


#4. bfs 탐색
count=0

global check
check=[[0 for x in range(w)] for y in range(h)]

for i in range(h):
    for j in range(w):
        # 호수인데 아직 탐색이 안된 곳
        if lack[i][j]=='L' and check[i][j]==0:
            bfs(i,j)
            count+=1


print(count)
