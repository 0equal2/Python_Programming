### 프로그래머스
### 2020 카카오 인턴십
### 수식 최대화



from collections import deque

def operation(a,b,x):
    if x=='+':
        return a+b
    elif x=='-':
        return a-b
    elif x=='*':
        return a*b

def cal(op,exp):
    
    for i in op:
        now_op=i # 현재 계산 할 연산자
        
        new_exp=deque()
        while exp:
            now=exp.popleft()
            
            if now==now_op:
                a=new_exp.pop()
                b=exp.popleft()
                c=operation(int(a),int(b),now_op)
                new_exp.append(c)
                
            else:
                new_exp.append(now)
                
        exp=new_exp
    
    #print(exp)
    return abs(int(exp.popleft()))
    

def solution(expression):
    answer = 0
    
    #1. 연산자 순위는 총 6가지이다.
    op=[['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','+','-'],['*','-','+']]

    #2. expression을 숫자와 연산자 분리하기
    exp=deque()
    num=''
    for i in expression:
        if i.isdigit(): #2-1.숫자일 경우 
            num+=i
        else: #2-2.연산자일 경우
            exp.append(num)
            exp.append(i)
            num=''
    exp.append(num) #2-3.***마지막 숫자까지 넣어주어야 함
    #print(exp)
    
    #3. 연산자의 경우의수 모두 해보기
    for i in range(len(op)):
        #4. ***원본을 훼손시키지 않기 위해 복사!!!! 
        exp2=exp.copy() 
        result=cal(op[i],exp2)
        
        #5. 가장 결과값이 큰 수로 업데이트 
        if answer<result:
            answer=result
    
    return answer
