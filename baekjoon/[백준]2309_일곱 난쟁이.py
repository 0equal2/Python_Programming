###백준 #2309
###일곱 난쟁이

from itertools import combinations

#1. 9난쟁이 키
arr=[]

for i in range(9):
    arr.append(int(input()))


#2. 정렬
arr.sort()


#3. 두명 제외 리스트
out=list(combinations([i for i in range(9)],2))
check=[1 for i in range(9)]


#4.
remain=sum(arr)-100

for x1,x2 in out:
    if remain==arr[x1]+arr[x2]:
        check[x1]=0
        check[x2]=0
        break

for i in range(9):
    if check[i]:
        print(arr[i])


