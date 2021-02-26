###백준 #7569
###토마토


from sys import stdin
from collections import deque
    


#1. m,n,h
m,n,h=map(int,stdin.readline().split())

#2. 토마토의 초기 상태
tomato=[]
unripe=0  #안익은 토마토 개수
ripe=deque()
check=[[0 for i in range(m)] for j in range(n*h)]

for i in range(n*h):
    line=list(map(int,stdin.readline().split()))
    tomato.append(line)

    #안익은 토마토 개수 세기
    for j in range(len(line)):
        if line[j]==0:
            unripe+=1
        if line[j]==1:
            ripe.append([i//n, i%n, j, 0])
            check[i][j]=1

#print(unripe)


#3.
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dh=[1,-1]


#4.
day=0


if unripe:
    while ripe:

        i,j,k,d=ripe.popleft()

        #위아래
        for x in dh:
            ni=i+x

            if 0<=ni<h:
                if tomato[(ni*n)+j][k]==0 and check[(ni*n)+j][k]==0:
                    check[(ni*n)+j][k]=1
                    tomato[(ni*n)+j][k]=1
                    unripe-=1
                    ripe.append([ni,j,k,d+1])

                    if d+1>day:
                        day=d+1


        #앞뒤왼오
        for x in range(len(dx)):
            nj=j+dx[x]
            nk=k+dy[x]

            if 0<=nj<n and 0<=nk<m:
                if tomato[(i*n)+nj][nk]==0 and check[(i*n)+nj][nk]==0:
                    tomato[(i*n)+nj][nk]=1
                    check[(i*n)+nj][nk]=1
                    unripe-=1
                    ripe.append([i,nj,nk,d+1])

                    if d+1>day:
                        day=d+1


        if unripe==0: #안익은 토마토의 개수
            break

    # 더이상 익을 토마토가 없는데 아직 안익은 토마토가 있는지 확인
    if unripe>0:
        print(-1)
        
    else:
        print(day)


        
else:
    print(day)
                

