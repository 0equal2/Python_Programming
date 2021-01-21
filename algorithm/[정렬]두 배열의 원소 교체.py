### [정렬] 두 배령의 원소 교체
### 이것이 취업을 위한 코딩 테스트다 with 파이썬


#1. n, k 입력받기
n, k = map(int,input().split())


#2. 배열 a,b
a=list(map(int,input().split()))
b=list(map(int,input().split()))


#3. 배열 정렬하기 (a: 오름차순, b: 내림차순)
a.sort()
b.sort(reverse=True)

print(a)
print(b)


#4. k번 스위치
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break

print(a)
print(b)
print("result : ", sum(a))
