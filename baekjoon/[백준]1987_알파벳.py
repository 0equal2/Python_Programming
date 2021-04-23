###백준 #1987
###알파벳

#from collections import deque
from sys import stdin

#1. r, c 입력받기
r,c=map(int,stdin.readline().split())

#2. board 입력받기
board=[]
for i in range(r):
    board.append(list(map(str,stdin.readline())))


#3.
length=1

dx=[0,0,1,-1]
dy=[1,-1,0,0]



#queue=deque()
#queue.append([0,0,board[0][0]])
queue=set([(0,0,board[0][0])])

while queue:
    #print(queue)
    #x,y,alpha=queue.popleft()
    x,y,alpha=queue.pop()
    #print(alpha)

    for i in range(len(dx)):
        nx,ny=x+dx[i],y+dy[i]
        #print('nx,ny,board[nx][ny]', nx,ny,board[nx][ny])

        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny] not in alpha:
                #queue.append([nx,ny,alpha+board[nx][ny]])
                queue.add((nx,ny,alpha+board[nx][ny]))
                
                length=max(length, len(alpha)+1)

            


print(length)
                
                

