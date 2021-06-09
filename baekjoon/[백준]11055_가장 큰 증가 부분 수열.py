###백준 #11055
###가장 큰 증가 부분 수열


#1. n
n=int(input())

#2.
arr=list(map(int,input().split()))

#3.
dp=[0 for i in range(n)]
dp[0]=arr[0]


for i in range(1,n):
    for j in range(i):
        if arr[j]<arr[i] and dp[j]>dp[i]:
            dp[i]=dp[j]

    dp[i]+=arr[i]


print(max(dp))
