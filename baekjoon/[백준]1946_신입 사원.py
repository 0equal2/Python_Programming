###백준 #1946
### 신입 사원

import sys


#1. 테스트 케이스의 개수 : T
T=int(sys.stdin.readline())


for t in range(T):

    #2. 지원자의 숫자
    n=int(sys.stdin.readline())

    #3. 지원자의 서류심사 성적, 면접 성적의 순위
    score=[]

    for i in range(n):
        score.append(list(map(int,sys.stdin.readline().split())))


    #4. 서류 심사 오름 차순 정렬
    score.sort()

    #5. 신입 사원 선발
    count=0

    #첫번째 사람은 무조건 채용
    first=score[0][0] #현재 서류 심사 순위
    second=score[0][1] #현재 면접 성적 순위
    count+=1

    for i in range(1,n):

        if first<score[i][0]:
            first=score[i][0]

            if second<score[i][1]:
                continue

            else:
                second=score[i][1]

        count+=1

    print(count)

 
