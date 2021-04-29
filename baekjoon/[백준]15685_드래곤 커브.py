###백준 #15685
###드래곤 커브

def make_dragon(x,y,d,g,check):
    
    #0세대 상태
    check[x][y]=1
    
    x,y=x+dx[d],y+dy[d]
    check[x][y]=1
    

    #방향 스택
    stack=[d]
    
    
    #g>=1 세대
    for i in range(g):
        length=len(stack)

        for j in range(length-1,-1,-1):
            #움직여야하는 방향
            nd=(stack[j]+1)%4

            x,y=x+dx[nd],y+dy[nd]
            check[x][y]=1

            stack.append(nd)

            #print(x,y)

            
            
            


#1. 드래곤 커브 개수: n
n=int(input())

#2. 방향 : 0,1,2,3 방향 순(오른, 위, 왼, 아래)
dx=[0,-1,0,1]
dy=[1,0,-1,0]


#3. 드래곤 커브 체크 보드
check=[[0 for i in range(101)] for j in range(101)]

#4.
for dragon in range(n):
    #4-1. 시작점, 방향, 세대 : x,y,d,g
    x,y,d,g=map(int,input().split())

    #4-2. 드래곤 그리기
    make_dragon(y,x,d,g,check)

#5. 사각형 카운트
count=0

for i in range(100):
    for j in range(100):
        if check[i][j]==1:
            if check[i+1][j]==1 and check[i][j+1]==1 and check[i+1][j+1]==1:
                count+=1

print(count)
        


    
