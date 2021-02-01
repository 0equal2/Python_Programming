### 프로그래머스
### 2019 KAKAO BLIND RECRUITMENT
### 오픈채팅방 

def solution(record):
    answer = []
    
    #유저아이디와 닉네임 저장 
    data=dict()
    
    #채팅방 로그
    log=[]
    
    for user in record:
        user=user.split(' ')
        
        if user[0]=="Enter":
            #1. 로그 남기기
            log.append([0,user[1]])
            #2. 유저아이디와 닉네임 업데이트
            data[user[1]]=user[2]
            
        elif user[0]=="Leave":
            #3. 로그 남기기
            log.append([1,user[1]])
            
        elif user[0]=="Change":
            #4. 유저아이디와 닉네임 업데이트
            data[user[1]]=user[2]
            
            
    #메세지 출력
    for state, userid in log:
        message=data[userid]+'님이 '
        
        if state==0:
            message+='들어왔습니다.'
        elif state==1:
            message+='나갔습니다.'
        
        answer.append(message)
        
        
            
    
    return answer
