###백준 #21608
###상어 초등학교


#조건 5-1.
def choose1(k,v,classroom):
    seat=dict()
    maxnum=0

    for x in range(n):
        for y in range(n):
            #빈자리라면 앉을 수 있는 자리
            if classroom[x][y]==0:
                count=0

                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]

                    if 0<=nx<n and 0<=ny<n:
                        #인접칸에 친한 친구가 있다면
                        if classroom[nx][ny] in v:
                            count+=1

                seat[count]=seat.setdefault(count,[])+[[x,y]]

                if maxnum<count:
                    maxnum=count

    return seat[maxnum]

#조건 5-2.
def choose2(k,seat,classroom):
    newseat=dict()
    maxnum=0

    for x,y in seat:
        count=0
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]

            if 0<=nx<n and 0<=ny<n:
                if classroom[nx][ny]==0:
                    count+=1

        newseat[count]=newseat.setdefault(count,[])+[[x,y]]

        if maxnum<count:
            maxnum=count

    return newseat[maxnum]



#1. 교실의 크기 : NxN
#학생의 수 : NxN
#N입력 : n
n=int(input())

#2. 교실 생성
classroom=[[0 for i in range(n)] for j in range(n)]

#3. 학생 정보
student=dict()
for i in range(n**2):
    info=list(map(int,input().split()))
    student[info[0]]=set(info[1:])


#4. 방향 벡터
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#5. 학생 자리 찾기
for k,v in student.items():

    #5-1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸 
    seat=choose1(k,v,classroom)

    #5-2. 5-1을 만족하는 칸이 여러개면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
    seat=choose2(k,seat,classroom)

    #5-3. 5-2를 만족하는 칸이 여러개면, 행과 열이 가장 작은 칸으로 자리 정함
    seat=sorted(seat)

    #5-4. 자리 배정
    classroom[seat[0][0]][seat[0][1]]=k



#6. 만족도 구하기
result=0
satisfaction=[0,1,10,100,1000]

for x in range(n):
    for y in range(n):
        #6-1. 현재 학생
        s=classroom[x][y]

        #6-2. 인접에 친한 친구 수
        count=0
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]

            if 0<=nx<n and 0<=ny<n:
                if classroom[nx][ny] in student[s]:
                    count+=1

        #6-3. 친한 친구 수만큼 만족도 더하기
        result+=satisfaction[count]
print(result)
