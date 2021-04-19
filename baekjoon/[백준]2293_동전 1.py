###백준 #2293
###동전 1

#1. 동전의 가지수 , 가치의 합 : n, k
n,k=map(int,input().split())


#2. 동전의 가치
coin=[]
for i in range(n):
    coin.append(int(input()))


#3.
dp=[0 for x in range(k+1)]
dp[0]=1

for i in coin:
    for j in range(1,k+1):
        if j-i>=0:
            dp[j]+=dp[j-i]



print(dp[k])
