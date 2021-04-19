###백준 #9205
#맥주 마시면서 걸어가기

from collections import deque


def dfs(n,loc,memo):
    festival=loc[-1]
    
    queue=deque()
    queue.append(loc[0])

    memo[0]=1

    while queue:
        x,y=queue.popleft()

        for i in range(n+2):
            if memo[i]==0:
                if abs(loc[i][0]-x)+abs(loc[i][1]-y)<=1000:
                    queue.append(loc[i])
                    memo[i]=1

    if memo[-1]==0:
        return 'sad'
    else:
        return 'happy'
    


#1. 테스트 케이스 개수 : t
t=int(input())

for i in range(t):
    #2. 편의점의 개수 : n
    n=int(input())

    #3. 위치 좌표
    loc=[]
    for j in range(n+2):
        loc.append(list(map(int,input().split())))

    #4. 방문 좌표
    memo=[0 for i in range(n+2)]

    #5. 탐색
    print(dfs(n,loc,memo))
    
