### 백준 #2468
### 코드업 #4697
### 안전 영역


from collections import deque

def bfs(x,y,rain,check):
    queue=deque()
    queue.append([x,y])
    check[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx and nx<n and 0<=ny and ny<n:
                if info[nx][ny]>rain and check[nx][ny]==0:
                    check[nx][ny]=1
                    queue.append([nx,ny])




#1. 행열개수 n
global n
n=int(input())


#2. 지역 정보
global info
info=[]

max_height=0 # 가장 높은 지역의 높이

for i in range(n):
    data=list(map(int,input().split()))
    info.append(data)
    max_height=max(max(data),max_height)


#3. 방향 벡터
global dx,dy
dx=[0,0,1,-1]
dy=[1,-1,0,0]



#4. 비의 양에 따른 안전 영역 개수
#비가 아예 안올 경우에는 안전 구역 1개
#비가 max_height까지 오면 안전 구역 0개 -> 이미 최소값...
result=[1] 

#비가 1부터 max_height-1까지 올 경우
for i in range(1,max_height):
    check=[[0 for x in range(n)] for y in range(n)]
    safe=0

    #지역보드 bfs 탐색
    for p in range(n):
        for q in range(n):
            if info[p][q]>i and check[p][q]==0: #안전 구역 발견!!
                bfs(p,q,i,check) #연결된 안전 구역 bfs로 방문 체크 해줌
                safe+=1
                
    result.append(safe)



print(max(result))

