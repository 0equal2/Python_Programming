### BFS 연결리스트 방문기본예제
### 이것이 코딩테스트다 with 파이썬


from collections import deque


# BFS 함수 정의 
def bfs(graph, start, visited):
    #큐를 생성
    queue=deque([start])
    #현재위치 방문처리
    visited[start]=True

    #큐 반복
    while queue:
        v=queue.popleft()
        print(v, end=' ')

        #아직 방문하지 않은 원소 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True




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




# 방문 체크 리스트
visited = [False] * 9


# bfs 함수 호출
bfs(graph, 1, visited)
