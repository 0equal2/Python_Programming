###백준 #11052
###카드 구매하기

#1. 민규가 구매하려고 하는 카드의 개수 : n
n=int(input())


#2. 1~n개가 들어있는 카드팩의 금액
m=[0]+list(map(int,input().split()))


#3.
dp=[0 for x in range(n+1)]

dp[1]=m[1]
dp[2]=max(m[1]*2, m[2])

for i in range(3, n+1):
    dp[i]=m[i]

    for j in range(1,i//2+1):
        dp[i]=max(dp[i],dp[j]+dp[i-j])
    

print(dp[n])
