### 미로 탈출 : 최소 이동 칸 수를 구하시오
### 스스로 풀이 
### 이것이 코딩테스트다 with 파이썬

from collections import deque

#bfs

def bfs(graph, x, y, visited):
    #시작점을 큐에 삽입
    queue=deque()
    queue.append([x,y,1])
    visited[x][y]=1


    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    

    while queue:
        a,b,c=queue.popleft()

        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]
            nc=c+1

            if na>=0 and na<n and nb>=0 and nb<m and graph[na][nb]==1 and visited[na][nb]==0:
                visited[na][nb]=nc
                queue.append([na,nb,nc])
                


# n, m을 입력받는데
n, m = map(int, input().split())


# 미로를 받는다
graph=[]

for i in range(n):
    arr=list(map(int, input()))
    graph.append(arr)



# 미로 방문 체크 그래프
visited=[[0]*m for _ in range(n)]


bfs(graph, 0, 0, visited)

#print(visited)
print(visited[n-1][m-1])


