###백준 #2573 
#빙산

from collections import deque
from sys import stdin

def bfs(x,y,iceberg,check):
    queue=deque()
    queue.append([x,y])
    check[x][y]=1

    while queue:
        x,y=queue.popleft()

        for i in range(len(dx)):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if check[nx][ny]==0 and iceberg[nx][ny]!=0:
                    check[nx][ny]=1
                    queue.append([nx,ny])

                    
                    
def melting(x,y,iceberg,check):

    check[x][y]=1

    for i in range(len(dx)):
        nx,ny=x+dx[i],y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if iceberg[nx][ny]==0 and iceberg[x][y]>0 and check[nx][ny]==0:
                iceberg[x][y]-=1

    if check[x][y]>0:
        return 1
    else:
        return 0
        
    
    
    

            
#1. n,m 입력
n,m=map(int,stdin.readline().split())

#2. 빙산 정보
iceberg=[]

for i in range(n):
    iceberg.append(list(map(int,stdin.readline().split())))


#3.
dx=[0,0,1,-1]
dy=[1,-1,0,0]


#4.
year=0

while True:
    

    #4-1. 빙산 녹기
    flag=0
    
    check=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j]!=0:
                if melting(i,j,iceberg,check):
                    flag=1

                #print(iceberg)

    #만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.
    if flag==0:
        year=0
        break
    
    
    check=[[0 for i in range(m)] for j in range(n)]
    count=0

    #4-2. 빙산 덩이 확인
    for i in range(n):
        for j in range(m):
            if check[i][j]==0 and iceberg[i][j]!=0:
                bfs(i,j,iceberg,check)
                count+=1

    
    
    if count>=2:
        year+=1
        break
    
    else:
        year+=1


print(year)
        
