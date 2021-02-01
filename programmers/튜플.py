### 프로그래머스
### 2019 카카오 개발자 겨울 인턴십
### 튜플

def solution(s):
    answer = []
    
    #1. 문자열 s에서 '{','}'를 빈문자열로 치환 후 ','를 기준으로 자른다.
    s=s.replace('{','')
    s=s.replace('}','')
    
    s=list(map(int, s.split(',')))
    
    #2. 딕셔너리를 생성하여 원소 카운트 하기
    data=dict()
    
    for i in s:
        data[i]=data.setdefault(i,0)+1
    
    #3. value값을 중심으로 data 딕셔너리 정렬
    data=sorted(data.items(), key=lambda t: t[1], reverse=True)
    
    #4. key값 순서대로 answer에 추가
    for k,v in data:
        answer.append(k)
    
    
    return answer
