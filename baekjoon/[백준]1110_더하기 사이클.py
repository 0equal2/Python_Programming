###백준 #1110
###더하기 사이클


#1. n 입력
n=int(input())

#2.
x=n
count=0

while True:
    count+=1
    
    #2-1. 각자리 수 더하기
    x2=(x//10)+(x%10)

    #2-2. x와 x2의 일의자리 합치기
    x=int(str(x%10)+str(x2%10))

    #2-3. 원래 수 확인
    if x==n:
        break


print(count)
