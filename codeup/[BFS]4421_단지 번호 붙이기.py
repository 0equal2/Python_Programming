### 코드업 #4421
### 단지 번호 붙이기


from collections import deque

def bfs(x,y,village,check):
    
    queue=deque()
    queue.append([x,y])
    check[x][y]=1

    count=1 #집의 수

    while queue:
        x,y=queue.popleft()

        #주변 탐색
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n:
                if village[nx][ny]==1 and check[nx][ny]==0:
                    check[nx][ny]=1
                    count+=1
                    queue.append([nx,ny])

    return count


#1. 지도의 크기 n
global n
n=int(input())

#2. 지도
village=[]

for i in range(n):
    village.append(list(map(int,input())))

#print(village)


#3.
result=[] #각 단지내 집의 수


#4. 방문 체크 
check=[[0 for x in range(n)] for y in range(n)]


#5. 방향 벡터
global dx,dy
dx=[0,0,1,-1]
dy=[1,-1,0,0]


#6. bfs 탐색
for i in range(n):
    for j in range(n):
        #집이면서 방문이 안 된 집일 경우 그 집을 기준으로 단지 탐색
        if village[i][j]==1 and check[i][j]==0:
            result.append(bfs(i,j,village,check))
            


#7. 각 단지내 집의 수를 오름차순으로 정렬
print(len(result))
result=map(str,sorted(result))
print('\n'.join(result))
