### 프로그래머스
### 2020 KAKAO BLIND RECRUITMENT
### 자물쇠와 열쇠 


def check(board,lock,n,m):
    #print(board)
    
    for i in range(n):
        for j in range(n):
            nx=m-1+i
            ny=m-1+j
            
            # key랑 겹치는 구간 
            if board[nx][ny]!=-1 :
                # 둘다 홈이거나 둘다 돌기인 경우
                if lock[i][j]==0 and board[nx][ny]==0:
                    return 0
                if lock[i][j]==1 and board[nx][ny]==1:
                    return 0
                
            # key랑 안겹치는 구간
            else:
                # lock은 홈인데 key로 채울 수 없는 경우 
                if lock[i][j]==0:
                    return 0

    return 1


# key를 반시계 방향으로 90도 회전 
def rotation(key,m):
    
    new_key=[[0 for x in range(m)] for y in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_key[m-j-1][i]=key[i][j]
    
    return new_key
    


def solution(key, lock):
    answer = True
    
    #1. lock, key의 길이 
    n=len(lock)
    m=len(key)
    
    
    #2. key를 한 칸씩 옮겨보기
    for i in range(m+n-1):
        for j in range(m+n-1):
            
            #3. 
            for k in range(4):
                
                #4. board판에 key를 옮겨준다.
                len_b=2*m+n-2
                board=[[-1 for x in range(len_b)] for y in range(len_b)]

                for p in range(m):
                    for q in range(m):
                        board[i+p][j+q]=key[p][q]
                    
                #print(board)
                
                #5. 열 수 있는지 확인
                if check(board,lock,n,m):
                    return answer
                
                #6. 못 연다면 key를 90도 회전 
                key=rotation(key,m)  
                #print(key)
                
    answer=False
    return answer
