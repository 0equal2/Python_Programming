### 프로그래머스
### 2020 KAKAO BLIND RECRUITMENT
### 블록 이동하기 


from collections import deque

def checkmove(i,nx0,ny0,nx1,ny1,board,d):
    # 바퀴가 보드를 벗어나는 경우
    if 0>nx0 or 0>ny0 or 0>nx1 or 0>ny1 or n<=nx0 or n<=ny0 or n<=nx1 or n<=ny1:
        return False

    # 바퀴 하나라도 1에 있을 경우
    if board[nx0][ny0]==1 or board[nx1][ny1]==1:
        return False
    
    # 가로방향인데 회전할 때
    if d:
        if i==4 :
            if board[x0+1][y0]==1:
                return False

        if i==5 :
            if board[x0-1][y0]==1:
                return False

        if i==6 :
            if board[x1-1][y1]==1:
                return False

        if i==7 :
            if board[x1+1][y1]==1:
                return False
    # 세로 방향인데 회전할 때 
    else:
        if i==4 :
            if board[x0][y0+1]==1:
                return False

        if i==5 :
            if board[x0][y0-1]==1:
                return False

        if i==6 :
            if board[x1][y1+1]==1:
                return False

        if i==7 :
            if board[x1][y1-1]==1:
                return False
    return True

def solution(board):
    answer = 0
    
    #1. 보드의 길이
    global n
    n=len(board)
    
    #2. 가로일 때 갈 수 있는 방향[왼, 오른]
    dx0=[[0,0],[0,0],[-1,-1],[1,1],[1,0],[-1,0],[0,-1],[0,1]]
    dy0=[[1,1],[-1,-1],[0,0],[0,0],[1,0],[1,0],[0,-1],[0,-1]]
    
    #3. 세로일 때 갈 수 있는 방향[위, 아래]
    dx1=[[0,0],[0,0],[-1,-1],[1,1],[1,0],[1,0],[0,-1],[0,-1]]
    dy1=[[1,1],[-1,-1],[0,0],[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    
    #4. 현재 위치
    global x0,y0,x1,y1
    x0,y0=0,0
    x1,y1=0,1
    
    #5. check
    check0=[[0 for i in range(n)] for j in range(n)]
    check1=[[0 for i in range(n)] for j in range(n)]
    
    #6. cost(움직이는 횟수)
    cost=[[0 for i in range(n)] for j in range(n)]
    
    
    #7. 
    queue=deque([[x0,y0,x1,y1,True,0]])
    
    while queue:
        data=queue.popleft()
        x0,y0=min(data[0],data[2]),min(data[1],data[3])
        x1,y1=max(data[0],data[2]),max(data[1],data[3])
        
        d=data[4] #현재 로봇의 방향
        move=data[5] #현재 로봇이 움직인 횟수 
        
        flag=0 #탐색이 가능한가 
        
        #가로방향에서 탐색을 하지않았던 경우라면 탐색 (d=True, check0[x0][y0]=0인 경우)
        if d:
            if check0[x0][y0]==0:
                check0[x0][y0]=1
                flag=1
        #세로 방향에서 탐색을 하지않았던 경우라면 탐색 (d=False, check1[x0][y0]=0인 경우) 
        else:
            if check1[x0][y0]==0:
                check1[x0][y0]=1
                flag=1
        
        #8가지 이동 경우 탐색 
        if flag:
            for i in range(8):
                if d:
                    ndx,ndy=dx0[i],dy0[i]
                else:
                    ndx,ndy=dx1[i],dy1[i]

                nx0,ny0=min(x0+ndx[0],x1+ndx[1]),min(y0+ndy[0],y1+ndy[1])
                nx1,ny1=max(x0+ndx[0],x1+ndx[1]),max(y0+ndy[0],y1+ndy[1])

                #새로운 위치로 움직일 수 있는가 
                if checkmove(i,nx0,ny0,nx1,ny1,board,d):
                    #i가 4이상인 경우 회전한 경우이므로 현재 방향에서 바꿔줌
                    if i<4:
                        nd=d
                    else:
                        nd=not d


                    cost[nx0][ny0]=min(cost[nx0][ny0],move+1) if cost[nx0][ny0]!=0 else move+1
                    cost[nx1][ny1]=min(cost[nx1][ny1],move+1) if cost[nx1][ny1]!=0 else move+1
                    
                    queue.append([nx0,ny0,nx1,ny1,nd,move+1])                 
        
    #print(cost)
    answer=cost[n-1][n-1]    
    
    return answer
