###백준 #2225
###합분해


#1. n, k입력
n,k=map(int,input().split())


#2.
dp=[[0 for i in range(201)] for j in range(201)]

for i in range(201):
    dp[i][1]=i
    dp[1][i]=1


for i in range(2,201):
    for j in range(2,201):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
        dp[i][j]=dp[i][j]%1000000000

print(dp[k][n])
