###백준 #11727
###2xn 타일링 2

#1. 가로의 길이 : n
n=int(input())

#2.
if n==1:
    print(1)
elif n==2:
    print(3)
else:
    dp=[0 for x in range(n+1)]

    #2-1. n=1인 경우 1가지
    dp[1]=1

    #2-2. n=2인 경우 3가지 (1x2 2개, 2x1 2개, 2x2 1개)
    dp[2]=3

    #2-3. dp[n]= dp[n-1] + (dp[n-2]*2)
    for i in range(3,n+1):
        dp[i]=dp[i-1] + (dp[i-2]*2)
        dp[i]=dp[i]%10007

    print(dp[n])




