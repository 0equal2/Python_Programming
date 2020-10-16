#https://0equal2.tistory.com/12

def lotate(key, M):
    temp=[[0 for i in range(M)] for j in range(M)]
    
    for i in range(M):
        for j in range(M):
            temp[i][j]=key[j][M-1-i]
    return temp


def keylocation(checkboard,key,a, b, M,N):
    #체크보드 -1로 초기화
    checkboard=[[-1 for i in range(M*2+N-2)] for j in range(M*2+N-2)]
    
    for i in range(M):
        for j in range(M):
            checkboard[i+a][j+b]=key[i][j]
            
    return checkboard
    
def resultcheck(key, lock, checkboard, M, N):
    
    #lock부분 check
    for i in range(N):
        for j in range(N):
            
            #7. checkboard[M-1+i][M-1+j]
            #7-1. key와 겹치는 부분이 아니다 
            if checkboard[M-1+i][M-1+j]==-1:
                #-> 홈이 있을 경우 false
                if lock[i][j]==0:
                    return False
            #7-2. key와 겹치는 부분이다
            else:
                #-> 같이 홈인 경우 false
                if lock[i][j]==0 :
                    if checkboard[M-1+i][M-1+j]==0:
                        return False
                #-> 같이 돌기인 경우 false
                elif lock[i][j]==1:
                    if checkboard[M-1+i][M-1+j]==1:
                        return False
    return True
                
    

def solution(key, lock):
    answer = True
    
    
    #1. 각자의 길이들
    M=len(key)
    N=len(lock)
    
    #1-1. lock이 다 1인경우 << 이 과정이 제일 찜찜
    count=0
    for i in range(N):
        for j in range(N):
            if lock[i][j]==0:
                count+=1
    if count==0:
        return True
    
    #2. key의 위치 checkboard 생성(-1 : 키 없음, 0 : 키 홈, 1 : 키 돌기)
    checkboard=[]
    
    #3. 키 위치 시키기
    for i in range(M+N-1):
        for j in range(M+N-1):
            #키의 시작 위치 [i,j]
    
            #4. 키 90도 회전 시키기
            for k in range(4):
                key=lotate(key,M)
                
                #5. 체크 보드 만들기
                checkboard=keylocation(checkboard, key, i, j, M, N)
                
                
                #6. 맞는지 확인하기
                if resultcheck(key, lock, checkboard, M, N):
                    return True
                
                
    return False
