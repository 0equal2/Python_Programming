###프로그래머스
###2020 KAKAO BLIND RECRUITMENT
###기둥과 보 설치

def install(x,y,a,pillar,floor,N):
    
    #기둥을 설치 할 수 있는 조건
    if a==0:
        #1. 바닥 위에 있거나
        if y==0:
            return 1
        #2. 보의 한쪽 끝 부분 위에 있거나
        if x==0:
            if floor[x][y]==1:
                return 1
        elif x==N:
            if floor[x-1][y]==1:
                return 1
        else:
            if floor[x][y]==1 or floor[x-1][y]==1:
                return 1
        #3. 다른 기둥 위에 있거나
        if y>0:
            if pillar[x][y-1]==1:
                return 1

        
    #보를 설치 할 수 있는 조건
    if a==1:
        #1. 한쪽 끝 부분이 기둥 위에 있거나
        if pillar[x][y-1]==1 or pillar[x+1][y-1]==1:
            return 1
        #2. 양쪽 끝 부분이 다른 보와 동시에 연결되거나
        if 0<x and x<N:
            if floor[x-1][y]==1 and floor[x+1][y]==1:
                return 1
    
    return 0


            
def remove(x,y,a,pillar,floor,N):

    #기둥인 경우 해당 기둥을 삭제
    if a==0:
        pillar[x][y]=0
    
    #보인 경우 해당 보를 삭제
    if a==1:
        floor[x][y]=0
        
    #삭제하였을 때 나머지 기둥, 보들이 설치 조건을 맞추었는지 확인
    for i in range(N+1):
        for j in range(N+1):
            if pillar[i][j]==1:
                if install(i,j,0,pillar,floor,N)==0:
                    return 0 
            if floor[i][j]==1:
                if install(i,j,1,pillar,floor,N)==0:
                    return 0
                
    return 1
        
        
        

def solution(n, build_frame):
    answer = []
    
    #[x,y,a,b]= [x,y,기둥보,삭제설치]
    #보는 교차점 기준 오른쪽, 기둥은 위쪽으로 설치
    
    pillar=[[0 for i in range(n+1)] for j in range(n+1)] #기둥이 설치될 수 있는 범위 0~N
    floor=[[0 for i in range(n+1)] for j in range(n+1)]  #보가 설치될 수 있는 범위 0~N-1
    
    
    #1. build_frame
    for x,y,a,b in build_frame:
        #2. 삭제 설치 구분 
        if b==0: # 삭제 
            
            if remove(x,y,a,pillar,floor,n):
                if a==0:
                    pillar[x][y]=0
                elif a==1:
                    floor[x][y]=0
                print("remove: ",x,y,a)
            else:
                if a==0:
                        pillar[x][y]=1
                elif a==1:
                        floor[x][y]=1    
                

        elif b==1: # 설치 
            if install(x,y,a,pillar,floor,n):
                if a==0:
                        pillar[x][y]=1
                elif a==1:
                        floor[x][y]=1
                        
                print("install: ",x,y,a)
                
                        
    
    #존재하는 기둥,보 추가
    for i in range(n+1):
        for j in range(n+1):
            if pillar[i][j]==1:
                answer.append([i,j,0])
            if floor[i][j]==1:
                answer.append([i,j,1])
                
                
    answer=sorted(answer)
                 
    
    
    return answer
