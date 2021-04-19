###백준 #5014
###스타트링크

#f: 총 1층부터 f층
#s: 강호가 지금 있는 층
#g: 스타트링크가 있는 층
#u: 위로 u층
#d: 아래로 d층

from collections import deque

def bfs(f,s,g,u,d):
    queue=deque()
    queue.append([s,0])

    visited={s}

    while queue:
        now,count=queue.popleft()

        #스타트링크에 도착하는 경우
        if now==g:
            return count

        #위층으로 갈 수 있는 경우  
        if (now+u)<=f and (now+u) not in visited:
            queue.append([now+u, count+1])
            visited.add(now+u)

        #아래층으로 갈 수 있는 경우
        if (now-d)>=1 and (now-d) not in visited:
            queue.append([now-d,count+1])
            visited.add(now-d)

    return 'use the stairs'


#1. f,s,g,u,d 입력
f,s,g,u,d=map(int,input().split())

#2.
print(bfs(f,s,g,u,d))

