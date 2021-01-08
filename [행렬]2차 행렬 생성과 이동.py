###2차 행렬 생성과 이동


n,m=map(int, input().split())


#2차 행렬 생성(nxm)

arr=[]

for i in range(n):
    rl=list(map(int, input().split()))
    arr.append(rl)



#동서남북
dx=[0,0,1,-1]
dy=[1,-1,0,0]


#현재 위치
x,y= 2,2


#이동 위치

for i in range(4): #동서남북 4가지 이동방향
    nx=x+dx[i]
    ny=y+dy[i]
    print(nx,ny, arr[nx][ny]) #이동위치, 해당 값


    



 
