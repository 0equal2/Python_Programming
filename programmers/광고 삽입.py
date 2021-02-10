### 프로그래머스
### 2021 KAKAO BLIND RECRUITMENT
### 광고 삽입



def to_seconds(time):
    h,m,s=map(int,time.split(':'))
    
    return h*3600+m*60+s

def to_time(time):
    h=str(time//3600).zfill(2)
    time=time%3600
    m=str(time//60).zfill(2)
    s=str(time%60).zfill(2)
    
    return ':'.join([h,m,s])
    

def solution(play_time, adv_time, logs):
    answer = ''
    
    #1. 계산하기 쉽게 play_time, adv_time, logs 초단위로 바꾸기
    play_time=to_seconds(play_time)
    adv_time=to_seconds(adv_time)
    
    #1-1. 시청자 수 메모 
    memo=[0 for _ in range(play_time+1)]
    
    for l in logs:
        s,e=map(str,l.split('-'))
        s=to_seconds(s)
        e=to_seconds(e)
        
        memo[s]+=1
        memo[e]+=-1
        
    #2. 누적 시청자 수 메모
    #2-1. 현재 시청자 수 
    for i in range(1,play_time+1):
        memo[i]=memo[i]+memo[i-1]
    #2-2. 누적 시청자 수 
    for i in range(1,play_time+1):
        memo[i]=memo[i]+memo[i-1]
    
    
    #3. 
    max_play=memo[adv_time-1]
    start=0
    
    for i in range(adv_time,play_time):
        play=memo[i]-memo[i-adv_time]
        
        if play>max_play:
            max_play=play
            start=i-adv_time+1
            
    answer=to_time(start)    
    
    return answer
