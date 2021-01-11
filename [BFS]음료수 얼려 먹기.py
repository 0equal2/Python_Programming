### 음료수 얼려 먹기
### 이것이 코딩테스트다 with 파이썬


def dfs(graph, x, y, visited):
    #현재 방문 체크
    visited[x][y]=True
    print(x,y)

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]


    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        #만약 새 위치가 그래프 이내이면서 방문하지 않았고 구멍이 뚫렸다면
        if nx>=0 and nx<n and ny>=0 and ny<m and not visited[nx][ny] and graph[nx][ny]==0:
            dfs(graph, nx, ny, visited)
            
    




# n,m 입력받기
n,m = map(int, input().split())


# 얼음판 입력받기
graph=[]

for i in range(n):
    array=list(map(int, input()))
    graph.append(array)



# 방문 체크
visited = [[False]*m for _ in range(n)]



print(graph)
print(visited)



count=0

for i in range(n):
    for j in range(m):

        if graph[i][j]==0 and not visited[i][j]:
            count+=1
            dfs(graph, i, j, visited)
            #print("cut")

        


print(count)


