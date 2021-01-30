### [프로그래머스]
### 2020 KAKAO BLIND RECRUITMENT
### 메뉴 리뉴얼

from itertools import combinations

def solution(orders, course):
    answer = []
    
    #1. 모든 메뉴 오름차순으로 정리
    for i in range(len(orders)):
        order=list(orders[i])
        order=sorted(order)
        orders[i]=''.join(order)
        
    
    
    #2. course만큼 부분집합 생성
    for i in course:
        menu=dict()
        combi=[]  #orders에서 만들어진 크기가 i인 부분집합들
        
        for j in orders:
            combi.extend(combinations(j,i))
        
        
        #3. 구해진 크기가 i인 부분집합들을 카운트하여 menu 딕셔너리에 저장
        # menu(k,v)=(부분집합, 개수)
        for j in combi:
            menu[j]=menu.setdefault(j,0)+1
            
        
        #4. 각 부분집합들 중에 가장 많이 주문된 횟수: max_num
        max_num=0
        
        if len(menu.values())!=0: #부분집합의 개수가 0이 아닐 때
            if max(menu.values())>max_num: #가장 많이 주문된 횟수는 ? 
                max_num=max(menu.values())
        
        #5. 최소 2번 이상은 주문되어야 세트메뉴를 구성할 수 있다. 
        if max_num>=2:
            for k,v in menu.items():
                if v==max_num:
                    k=''.join(list(k))
                    answer.append(k)
        
        #6. 정렬하여 출력
        answer=sorted(answer)        
    
    return answer
