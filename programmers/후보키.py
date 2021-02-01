### 프로그래머스
### 2019 KAKAO BLIND RECRUITMENT
### 후보키


from itertools import combinations
candidate=[]

# 유일성 확인하기 
def uniqueness(r,c):
    student=[]
    
    for x in r:
        data=[]
        for i in c:
            data.append(x[i])
        student.append(tuple(data))
    
    if len(set(student))==len(r):
        return 1
    else:
        return 0

# 최소성 확인하기
def minimality(c):
    for x in candidate:
        if x.issubset(c):
            return 0
    return 1
    

def solution(relation):
    answer = 0
    
    #1. 컬럼 수 
    n=len(relation[0])
    attri=[i for i in range(n)]
    
    #2. 후보키가 될 수 있는 조합 경우의 수 
    combi=[]
    for i in range(1,n+1):
        combi.extend(map(set,combinations(attri,i)))
    
    #3. 유일성 최소성 확인
    for i in combi:
        if minimality(i):
            if uniqueness(relation,i):
                answer+=1
                candidate.append(i)
                
    
    return answer
