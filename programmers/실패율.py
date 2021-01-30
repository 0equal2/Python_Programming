### 프로그래머스
### 2019 KAKAO BLIND RECRUITMENT
### 실패



def solution(N, stages):
    answer = []
    
    #1. 실패율 딕셔너리 : k,v= 스테이지번호, 실패율
    fail=dict()
    
    for i in range(1,N+1):
        step=0 # i 스테이지에 도달한 플레이어 수 
        stay=0 # i 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 
        
        for j in stages:
            if i==j: # i 스테이지에 도달했으나 클리어 못함 
                stay+=1
                step+=1
            elif i<j: # i 스테이지에 도달하였고 클리어 함
                step+=1
                
        # *** 실패율 구할 때 나누는 수가 0이면 안됨. 
        # 다시 말해, step이 0일 경우 실패율은 0으로 처리
        if step==0:
            fail[i]=0
        else:
            fail[i]=stay/step
    
    # value 값을 기준으로 내림차순으로 정렬
    fail=sorted(fail.items(), key=lambda t:t[1], reverse=True)
    
    # key값을 순서대로 추가
    for i in range(len(fail)):
        answer.append(fail[i][0])
    
    return answer
