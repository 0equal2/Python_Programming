### 백준 #1697
### 숨바꼭질

from collections import deque

#1. n, k
n,k=map(int, input().split())


#2. check
check=[0 for _ in range(100001)]


#3. bfs
queue=deque()
queue.append([n,0])

result=0

while queue:
    n,move=queue.popleft()

    if check[n]==0:
        check[n]=1

        if n==k:
            result=move
            break

        if (n+1)<=100000:
            queue.append([n+1,move+1])

        if (n*2)<=100000:
            queue.append([n*2,move+1])

        if (n-1)>=0:
            queue.append([n-1,move+1])

print(result)
            



