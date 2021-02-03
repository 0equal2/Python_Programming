### 프로그래머스
### 2020 카카오 인턴십
### 경주로 건설


from collections import deque

def move(d,nd):
    #커브인 경우 <***직선+커브값이기 때문에 600원을 더해주어야한다.>
    if (d=='R' or d=='L') and (nd=='U' or nd=='D'):
        return 600
    elif (d=='U' or d=='D') and (nd=='R' or nd=='L'):
        return 600
    
    #직선인 경우
    else:
        return 100
    
    
def search(x,y,c,d,board):
    n=len(board)  
    result=[]
    
    # 방향
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    D=['R','L','U','D']
    
    # bfs 탐색 준비
    queue=deque()
    queue.append([x,y,c,d])
    memo=[[0 for x in range(n)] for y in range(n)]
    memo[x][y]=1
    
    while queue:
        x,y,c,d=queue.popleft()
        
        #목표 지점
        if x==n-1 and y==n-1:
            result.append(c)
            continue
            
        #방향 확인
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            
            if 0<=nx and nx<n and 0<=ny and ny<n:
                if board[nx][ny]==0:
                    nc=c+move(d,D[i])
                    
                    # 가지 않았던 곳이거나 최소값으로 업데이트 되는 경우 탐색 추가
                    if memo[nx][ny]==0 or nc<memo[nx][ny]:
                        memo[nx][ny]=nc
                        queue.append([nx,ny,nc,D[i]])
    
    
    return min(result)
    


def solution(board):
    answer = 0
    
    n=len(board)
    
    # 우선  처음에는 두가지 방향으로 움직일 수 있다.
    an1=search(0,0,0,'R',board)
    an2=search(0,0,0,'D',board)
    
    # 두 방향의 결과중에 가장 최소 값
    answer=min(an1,an2)
    
    
    return answer
