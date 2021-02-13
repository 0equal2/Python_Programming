### 백준 #2606
### 바이러스

from collections import deque

#1. 컴퓨터 개수
n=int(input())

#2. 연결정보
line=int(input())
com=dict()

for i in range(line):
    x,y=map(int,input().split())
    com[x]=com.setdefault(x,[])+[y]
    com[y]=com.setdefault(y,[])+[x]

#print(com)


#3.
check=[0 for _ in range(n+1)]

queue=deque()
queue.append(1)
check[1]=1
count=0

while queue:
    now=queue.popleft()

    for new in com[now]:
        if check[new]==0:
            check[new]=1
            count+=1
            queue.append(new)


print(count)
