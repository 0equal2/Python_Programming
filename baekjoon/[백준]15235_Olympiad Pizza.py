###백준 #15235
#Olympiad Pizza


#문제 요약#
"""
n명의 사람이 피자를 먹기위해 줄을 서있다.
각 사람은 한조각씩 순서대로 받는다.

피자를 더 먹고 싶은 사람은 줄 맨 뒤에 다시 서서 피자를 기다린다.

몇번의 피자 배부끝에 배를 채울 수 있는가. 

"""

from collections import deque

#1. 사람 수 : n
n=int(input())

#2. 각 사람마다 먹어야 하는 피자 수
pizza=list(map(int,input().split()))


#3. 각 사람마다 피자 배부가 완료된 횟수
memo=[0 for i in range(n)]

#4. 
queue=deque()

for i in range(n):
    queue.append([i,0])

#5.
count=0

while queue:
    num,get=queue.popleft() #사람번호, 받은 피자 수 
    count+=1

    get+=1

    if pizza[num]==get:
        memo[num]=count #몇번 배부끝에 배를 채웠는지

    else:
        queue.append([num,get])


#6.
memo=map(str,memo)

print(' '.join(memo))



    
