###프로그래머스
###2019 카카오 개발자 겨울 인턴십
###불량 사용자

from itertools import permutations

def check(b,u):
    if len(b)!=len(u):
        return 0
    
    for i in range(len(b)):
        if b[i]!='*':
            if b[i]!=u[i]:
                return 0
                
    return 1

def compare(b_list,u_list):
    
    for i in range(len(b_list)):
        if not check(b_list[i],u_list[i]):
            return 0
    
    return 1

def solution(user_id, banned_id):
    answer = 0
    
    case=map(list,(permutations(user_id, len(banned_id))))
    result=[]
    
    for user_list in case:
        if compare(banned_id,user_list):
            result.append(sorted(user_list))
            
    result=map(tuple,result)
    answer=len(set(result))
    
    
    return answer
