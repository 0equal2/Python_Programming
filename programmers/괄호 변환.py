### 프로그래머스
### 2020 KAKAO BLIND RECRUITMENT
### 괄호 변환


from collections import deque

def iscorrect(w):
    #올바른 문자열인지 확인
    
    count=0
    
    for i in w:
        if i=='(':
            count+=1
        elif i==')':
            count-=1
        
        if count<0:
            return 0
    
    return 1
    

def balance(w):
    
    #1. 빈 문자열인 경우 빈 문자열을 반환
    if w=='':
        return w
    
    #2. w를 u,v로 분리
    count=0 # '(': +1, ')': -1
    u=''
    v=''
    w=deque(w)
    
    while w:
        x=w.popleft()
        if x=='(':
            count+=1
        elif x==')':
            count-=1
        
        u+=x
        
        if count==0: #괄호가 짝이 맞는 밸런스 괄호 일때 
            break
            
    v=''.join(w)
    
    
    #3. 문자열 u가 올바른 괄호면 v를 다시 1부터 수행
    if iscorrect(u):
        return u+balance(v)
    
    #4. u가 올바른 괄호가 아니라면
    else:
        #4-1.
        temp='('
        #4-2. 
        temp+=balance(v)
        #4-3.
        temp+=')'
        #4-4.
        u=u[1:-1]
        
        for i in u:
            if i=='(':
                temp+=')'
            elif i==')':
                temp+='('
        #4-5.
        return temp
        
        
        


def solution(p):
    answer = ''
    
    answer=balance(p)
    
    return answer
