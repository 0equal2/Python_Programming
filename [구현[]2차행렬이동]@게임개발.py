###[구현]2차행렬 이동_게임개발
##이것이 취업을 위한 코딩 테스트다 with 파이썬


#1. n,m입력을 받는다
n,m= map(int, input().split())

#2. 캐릭터의 위치와 방향을 입력받는다
x,y,z=map(int, input().split())

#3. 게임 맵을 입력받는다 (1:바다, 0:육지)
arr=[]

for i in range(n):
    temp=list(map(int, input().split()))
    arr.append(temp)


#4. 방문을 입력받을 맵
d=[[0]*m for _ in range(n)]
d[x][y]=1  #현재 위치 방문 처리 



#5. 방향 벡터(현재 방향을 기준으로 왼쪽부터)
# 북 동 남 서 : 0 1 2 3
dx=[-1,0,1,0]
dy=[0,1,0,-1]




#6. 왼쪽으로 회전
def turn_left():
    global z
    z-=1
    if z<0:
        z=3





#7. 게임 시작
count=1   #현재위치도 방문 포함이기 때문에 
turn_time=0


while True:
    #7-1. 왼쪽으로 회전
    turn_left()
    nx=x+dx[z]
    ny=y+dy[z]

    #7-2. 만약 정면에 육지고 안가본 곳이라면 이동
    if d[nx][ny]==0 and arr[nx][ny]==0:
        d[nx][ny]=1  #이동위치 방문표시
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue


    #7-3. 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1



    #7-4. 4방향 모두 갈 수 없는 경우
    if turn_time==4:
        nx=x-dx[z]
        ny=y-dy[z]

        #뒤로 갈 수 있다면 이동
        if arr[nx][ny]==0:
            x=nx
            y=ny

        #갈 수 없다면
        else:
            break

        turn_time=0



print(count)


    

    
            
