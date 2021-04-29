###백준 #9465
###스티커


#1. 테스트케이스 : testcase
testcase=int(input())

for t in range(testcase):
    #2. 스티커 가로 길이 : n
    n=int(input())

    #3. 스티커 점수
    score=[]
    for i in range(2):
        score.append(list(map(int,input().split())))

    #4. dp
    score[0][1]+=score[1][0]
    score[1][1]+=score[0][0]

    
    for j in range(2,n):
        score[0][j]+=max(score[1][j-1],score[1][j-2])
        score[1][j]+=max(score[0][j-1],score[0][j-2])

    print(max(score[0][n-1], score[1][n-1]))
