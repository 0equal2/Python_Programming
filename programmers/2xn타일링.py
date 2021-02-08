###프로그래머스
###연습문제
###2xn타일


def solution(n):
    answer = 0
    
    #1. 경우의 수 메모
    memo=[0 for _ in range(n)]
    
    #2. 
    for i in range(n):
        #i==0일 경우 가능한 경우 1가지 (세로타일 1개)
        if i==0:
            memo[i]=1
        #i==1일 경우 가능한 경우 1가지 (가로타일 2개)
        elif i==1:
            memo[i]=2
        else:
            memo[i]+=(memo[i-1]+memo[i-2])%1000000007
    
    answer=memo[-1]
            
    
    return answer
