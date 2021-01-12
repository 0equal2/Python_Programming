### 그리디 욕심쟁이 거스름돈
### codeup 3301

### 이 문제를 O(1)만에 풀 수 있다고 ??



# 거스름돈
n=int(input())


# 화폐 종류
arr=[50000,10000,5000,1000,500,100,50,10]

#

count=0


for i in arr:
    count+=n//i
    n=n%i


print(count)
