###백준 #11053
###가장 긴 증가하는 부분 수열

#이문제는 DP문제이다.

#1. n입력
n=int(input())

#2. 배열 입력
arr=list(map(int,input().split()))


#3. dp배열
dp=[0 for i in range(n)]
dp[0]=1

for i in range(1,n):
    max_num=dp[i]
    for j in range(i):
        if arr[j]<arr[i]:
            if max_num<dp[j]:
                max_num=dp[j]

    dp[i]=max_num+1

#print(dp)
print(max(dp))
