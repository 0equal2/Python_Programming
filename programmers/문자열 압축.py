### 프로그래머스
### 2020 KAKAO BLIND RECRUITMENT
### 문자열 압축


def solution(s):
    answer = 0
    
    #1. s의 길이
    n=len(s)
    answer=n  # 기존 s의 길이가 가장 길었을 때 길이
    
    
    #2. 문자열 자를 수 있는 단위 i : 1~(n//2)개
    for i in range(1, (n//2)+1):
        new_s=s  
        prev=''  # 이전 잘린 문자열
        count=1  # 같은 문자열의 수 
        result='' # 압축된 결과 저장 
        
        while len(new_s)>=i: 
            now=new_s[:i]  # new_s를 i만큼 자름 
            new_s=new_s[i:] # 자르고 남은 부분을 저장 
            
            if prev==now: # 현재 자른 부분과 이전에 잘린 문자열이 같다면 count + 1
                count+=1
            else:  # 현재 자른 부분과 이전에 잘린 문자열이 다르면 
                
                if count!=1: # 중복된 수를 먼저 적어주고 (1이 아닐경우에만 !) 
                    result+=str(count)
                    
                result+=prev # 이전 문자열을 추가
                prev=now
                count=1
        
        # 마지막 문자열 정리 
        if count!=1:
            result+=str(count)
        result+=prev    
        result+=new_s
        
        # 가장 짧은 압축된 문자열 길이로 업데이트 
        if answer>len(result):
            answer=len(result)
        
        
    
    return answer
