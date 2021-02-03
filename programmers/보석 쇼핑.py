###프로그래머스
###2020 카카오 인턴십
###보석 쇼핑



def solution(gems):
    answer = [0,0]
    
    #1. 보석의 종류, gems의 길이
    n=len(set(gems))
    length=len(gems)
    
    geminfo=dict()
    
    #2. 슬라이스윈도우 기법
    left,right=0,0
    case=[]
    
    while True:
        
        count=len(geminfo)
        
        #3. 모든 보석을 포함하는 경우
        if count==n:
            #3-1. 조건 만족 case에 추가해준다.
            case.append([left,right])
            #3-2. left에 있는 것 하나를 뺀다
            geminfo[gems[left]]-=1
            #3-3. 만약 뺀 것이 0이 된다면 geminfo에서 삭제
            if geminfo[gems[left]]==0:
                del geminfo[gems[left]]
            #3-4. start+1을 해주고 다시 루프
            left+=1
            continue
        
        
        #4. 만약 right가 length가 되면 break 
        if right==length:
            break
            
        #5. 만약 종류가 부족하다면 다음 쥬얼을 추가해 주고 right를 +1
        geminfo[gems[right]]=geminfo.setdefault(gems[right],0)+1    
        right+=1
        
        
    #6. 가능한 case중에서 가장 짧은 것을 선택 
    short=length+1
    for l,r in case:
        if short>r-l:
            short=r-l
            answer=[l+1,r]
    
    
    return answer
