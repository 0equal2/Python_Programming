###백준 #2133
###타일 채우기

#1. 가로 크기 : n
n=int(input())

#2.
if n==1:
    print(0)
elif n==2:
    print(3)
elif n==3:
    print(0)
else:
    dp=[0 for x in range(n+1)]

    dp[0]=1
    dp[2]=3

    for i in range(4,n+1):
        if i%2==0:
            dp[i]=dp[i-2]*3

            for j in range(4,i+1,2):
                dp[i]+=dp[i-j]*2

    print(dp[n])
