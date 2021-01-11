### DFS 연결리스트 재귀 방문기본예제
### 이것이 코딩테스트다 with 파이썬



# DFS 함수정의
def dfs(graph, v, visited):
    #현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    #다음 노드 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



# 연결리스트로 그래프 표현
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]


# 방문 체크
visited=[False]*9

# DFS 호출
dfs(graph, 1, visited)
