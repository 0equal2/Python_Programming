### 백준 #1920
### 수 찾기



#1. n입력
n=int(input())

#2. n개의 정수
arr=list(map(int,input().split()))
arr=sorted(arr)

#3. m입력
m=int(input())

#4. m개의 정수
find=list(map(int,input().split()))



# find에 있는 각 원소가 arr에 있다면 1 없다면 0 출력
for i in range(m):
    left=0
    right=n-1

    check=0  #있다면 1 없다면 0


    while left<=right:
        
        mid=(left+right)//2

        if find[i]>arr[mid]:
            left=mid+1

        elif find[i]<arr[mid]:
            right=mid-1

        else:
            check=1
            break

    print(check)
        
        
    
