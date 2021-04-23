###백준 #2156
###포도주 시식

#1. 포도잔의 개수 : n
n=int(input())

#2. 포도주의 양
wine=[0]
for i in range(n):
    wine.append(int(input()))


#3.
if n==1:
    print(wine[1])

elif n==2:
    print(wine[1]+wine[2])

else:
            
    dp=[0 for i in range(n+1)]

    dp[1]=wine[1]
    dp[2]=wine[1]+wine[2]
    
    for i in range(3,n+1):
        dp[i]=max(max(dp[:i-1])+wine[i],max(dp[:i-2])+wine[i-1]+wine[i])


    print(max(dp))
