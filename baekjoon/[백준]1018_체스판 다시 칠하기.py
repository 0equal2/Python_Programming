###백준 #1018
###체스판 다시 칠하기

#1. m,n 입력받기
m,n=map(int,input().split())

#2. board 정보
board=[]
for i in range(m):
    board.append(list(map(str,input())))


#3. 완전 탐색
result=m*n


for i in range(m-8+1):
    for j in range(n-8+1):

        first_b=0
        first_w=0

        for p in range(8):
            for q in range(8):

                if (p+q)%2==0:
                    if board[i+p][j+q]=='W': first_b+=1
                    if board[i+p][j+q]=='B': first_w+=1

                else:
                    if board[i+p][j+q]=='B': first_b+=1
                    if board[i+p][j+q]=='W': first_w+=1

        result=min(result,min(first_b,first_w))


print(result)
