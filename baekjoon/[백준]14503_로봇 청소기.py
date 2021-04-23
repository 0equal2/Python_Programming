###백준 #14503
###로봇 청소기

from collections import deque


#1. 세로크기, 가로크기: n,m
n,m=map(int,input().split())

#2. 로봇 청소기의 칸 (r,c) , 바라보는 방향 d
r,c,d=map(int, input().split())

#3. board 정보
board=[]

for i in range(n):
    board.append(list(map(int,input().split())))

#4. 청소 시작

#4-0. 초기상태 
check=[[0 for x in range(m)] for y in range(n)] #방문 체크
queue=deque([[r,c,d]])
#움직이는 방향 (북, 동, 남, 서)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#4-1. 현재 위치를 청소한다.
check[r][c]=1
count=1

while queue:
    #4-2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색
    r,c,d=queue.popleft()
    

    #4-2-a. 왼쪽 방향에 청소하지 않은 공간이면 회전하고 전진
    #4-2-b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번
    nd=d #움직일 방향
    move=0 #움직일 수 있는가.
    
    for i in range(4):
        nd-=1
        if nd<0:
            nd=3
        #움직일 방향이 청소를 하지 않았다면
        nr,nc=r+dx[nd], c+dy[nd]
    
        if 0<=nr<n and 0<=nc<m:
            if board[nr][nc]==0 and check[nr][nc]==0:
                check[nr][nc]=1
                queue.append([nr,nc,nd])
                count+=1
                move=1
                break

    #4-2-c. 모두 청소가 이미 되어있거나 벽인 경우, 바라보는 방향을 유지한 채로 한칸 후진
    if move==1:
        continue
    else:
        nr,nc=r-dx[nd],c-dy[nd]
        if 0<=nr<n and 0<=nc<m:
            if board[nr][nc]==0:
                queue.append([nr,nc,nd])
                

print(count)


