### 코드업 #2633
### Lower Bound


#1.
n,k=map(int,input().split())

#2.

arr=list(map(int,input().split()))

#3.
left=0
right=n


while left<right:
    mid=(left+right)//2


    if arr[mid]<k:
        left+=1

    elif arr[mid]>=k:
        right-=1



print(left+1)
