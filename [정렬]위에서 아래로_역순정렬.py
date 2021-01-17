### [정렬] 위에서 아래로
### 이것이 취업을 위한 코딩 테스트다 with 파이썬

#1. n 입력
n=int(input())


#2. 숫자 리스트 입력
arr=[]
for i in range(n):
    arr.append(int(input()))

print(arr)


#3. 역순 정렬
#arr.sort(reverse=True)
arr=sorted(arr, reverse=True)


print(arr)
