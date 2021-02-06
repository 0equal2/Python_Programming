### 백준 #2805
### 나무 자르기

from sys import stdin

#1. 나무의 수 n, 가져가려는 나무의 길이 m
n,m=map(int,stdin.readline().split())

#2.
tree=list(map(int,stdin.readline().split()))


#3. 이분 탐색

left=0   #최소
right=max(tree)  #최대



while left<=right:
    mid=(left+right)//2

    #가져 갈 수 있는 나무 길이
    get=0 

    for i in range(0,n):
        #print(left, right, mid, i)
        if tree[i]-mid>0:
            get+=tree[i]-mid
            

    #가능한 부분중에 가장 높은 높이(환경 보호 이유)
    if get>=m:
        left=mid+1
    elif get<m:
        right=mid-1


print(right)

