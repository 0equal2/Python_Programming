###[그리디]큰 수의 법칙
###이것이 취업을 위한 코딩 테스트다 with 파이썬


#1. n,m,k를 입력받는다 
n,m,k= map(int, input().split())


#2. 배열을 입력받는다
arr=list(map(int, input().split()))


#3. 배열을 정렬한다 (내림차순)
arr.sort(reverse=True)


#4-1. 제일 큰 수와 두번째로 큰 수를 이용하여 문제해결 
s=0
count=0
index=0

for i in range(m):
    if count==k:
        s+=arr[index+1]
        count=0
        continue

    s+=arr[index]
    count+=1


print(s)


#4-2. 반복되는 덧셈 배열을 이용하여 구하기
max1=arr[0]
max2=arr[1]

s=(max1*k)+max2 
result=(m//(k+1))*s+(m%(k+1))*max1
print(result)

