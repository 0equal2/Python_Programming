### 코드업 #3500
### 지뢰 찾기 2


from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    check[x][y]=1
    
    while queue:
        x,y=queue.popleft()

        count=0 #현 지점의 주변 지뢰 확인
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n:
                if mine[nx][ny]==1:
                    count+=1
        minecount[x][y]=count
        
        #만약 주변에 지뢰가 있다면 주변 탐색 추가 x
        if count>0:
            continue
        
        #주변에 지뢰가 없다면 주변 탐색 추가 o 
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx and nx<n and 0<=ny and ny<n:
                if check[nx][ny]==0 and mine[nx][ny]==0:
                    check[nx][ny]=1
                    queue.append([nx,ny])

                 


#1. 지뢰 찾기 맵 정보
n=9  # 9x9 크기
mine=[]

for i in range(n):
    mine.append(list(map(int,input().split())))


#2. 시작 점
x,y=map(int,input().split())


#3. 방향 벡터(대각선포함)
dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]


#4.
check=[[0 for x in range(n)] for y in range(n)]
minecount=[[0 for x in range(n)] for y in range(n)]


#5.
#5-1.시작 점이 지뢰이면
if mine[x-1][y-1]==1:
    check[x-1][y-1]=1
    minecount[x-1][y-1]=-1

#5-2. 시적 점이 지뢰가 아니면
else:
    bfs(x-1,y-1)

    

#6. 출력
for i in range(n):
    for j in range(n):
        
        #6-1. check가 1인 경우 minecount 출력, 0인 경우 _ 출력
        if check[i][j]==1:
            print(minecount[i][j],end=' ')

        else:
            print('_',end=' ')
        
    print()

