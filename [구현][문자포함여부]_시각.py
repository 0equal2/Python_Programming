###[구현]문자 포함 여부_시각
###이것이 취업을 위한 코딩 테스트다  with  파이썬


#n을 입력받는다
n=int(input())



#00시 00분 00초부터  N시 59분 59초까지 모든 시각중에서 3이 하나라도 포함되는가 탐색

count=0

for i in range(n+1):
    for j in range(60):
        for k in range(60):

            if '3' in (str(i)+str(j)+str(k)):
                count+=1



print(count)
