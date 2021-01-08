###[그리드]1이 될 때까지
######이것이 취업을 위한 코딩 테스트다 with 파이썬


#1. n과 k를 입력받는다
n,k=map(int,input().split())

#2.
count=0

while True:
    #만약 n이 1이면 break
    if n==1:
        break
    
    #만약 n이 k의 배수면 
    if (n%k)==0:
        n=n//k

    else:
        n-=1

    count+=1
    

print(count)
