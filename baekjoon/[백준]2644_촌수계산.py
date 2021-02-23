###백준 #2644
#촌수계산

from collections import deque

#1. 사람 수 입력 : n
n=int(input())


#2. 두사람의 번호
p,q=map(int,input().split())


#3. 관계 수 입력 : m
m=int(input())


#4. 부모 자식간의 관계
relation=dict()

for i in range(m):
    x,y=map(int,input().split())

    relation[x]=relation.setdefault(x,[])+[y]
    relation[y]=relation.setdefault(y,[])+[x]


#print(relation)


#5. 촌수계산
queue=deque()
queue.append([p,0])


check=[0 for i in range(n+1)]
check[p]=1

result=-1

while queue:
    x,d=queue.popleft()

    for y in relation[x]:
        if y==q:
            result=d+1
            break

        if check[y]==0:
            queue.append([y,d+1])
            check[y]=1

    if result>-1:
        break

print(result)
