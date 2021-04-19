###프로그래머스 
###스택/큐
###기능개발

from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    #1. 오늘 날
    today=0
    
    #2. 첫 작업 완성날을 기준
    today=math.ceil((100-progresses[0])/speeds[0])
    count=1
    
    for i in range(1,len(progresses)):
        #2-1. 
        p=progresses[i]
        p+=today*speeds[i]
        
        #2-2. 작업이 완성 안된 경우
        if p<100:
            today+=math.ceil((100-p)/speeds[i])
            answer.append(count)
            count=1
        
        #2-3. 작업이 완성 된 경우
        else:
            count+=1
    
    answer.append(count)
    #print(answer)
    
    
    return answer
