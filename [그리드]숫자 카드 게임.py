###[그리드]숫자 카드 게임
###이것이 취업을 위한 코딩 테스트다 with 파이썬


import math

#1. n,m을 입력받는다
n, m = map(int, input().split())

#2. result 구하기

result=0

for i in range(n):
    arr=list(map(int, input().split()))

    min_v=min(arr)

    result=max(result, min_v)


print(result)
    
