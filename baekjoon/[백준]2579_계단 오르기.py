###백준 #2579
###계단 오르기

#1. 계단의 개수 : n
n=int(input())

#2. 계단의 점수
score=[0]
for i in range(n):
    score.append(int(input()))


#3.
if n==1:
    print(score[1])

elif n==2:
    print(score[1]+score[2])

else:
            
    dp=[0 for i in range(n+1)]

    dp[1]=score[1]
    dp[2]=score[1]+score[2]
    
    for i in range(3,n+1):
        dp[i]=max(dp[i-2]+score[i],dp[i-3]+score[i-1]+score[i])


    print(dp[n])
