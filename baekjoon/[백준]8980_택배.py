###백준 #8980
#택배

#1. 마을 수, 트럭의 용량 : n,c
n,c=map(int,input().split())

#2. 박스의 정보 개수
m=int(input())

#3. 박스의 정보
info=[]

for i in range(m):
    info.append(list(map(int,input().split())))

#4. 도착지, 받는지 순서로 정렬한다.
info=sorted(info, key=lambda x : (x[1],x[0]))


#5. 해당 마을에서 실을 수 있는 용량 메모
memo=[c for i in range(n+1)]

#6.
result=0

for i in range(m):
    start=info[i][0]
    end=info[i][1]

    move=min(memo[start:end])
    move=min(move,info[i][2])


    for j in range(start,end):
        memo[j]-=move

    result+=move

print(result)
