### 코드업 #4503
### 바이러스


from collections import deque


#1. 컴퓨터의 수
n=int(input())

#2. 직접 연결되어 있는 컴퓨터 쌍의 수
pair=int(input())

#3.
info=dict()

for i in range(pair):
    com1,com2=map(int, input().split())

    info[com1]=info.setdefault(com1,[])+[com2]
    info[com2]=info.setdefault(com2,[])+[com1]



#4. 탐색한 컴퓨터 체크
check=[0]*(n+1)
queue=deque()
queue.append(1)
check[1]=1

count=0

while queue:
    x=queue.popleft()

    for com in info[x]:
        if check[com]==0:
            check[com]=1
            queue.append(com)

            count+=1



print(count)

        
